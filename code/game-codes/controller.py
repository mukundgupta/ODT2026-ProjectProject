"""
controller.py — Movement decision system and ESP32 communication.

Responsibilities:
  - Read keyboard input (WASD / arrow keys) to determine desired command
  - Simulate the move by shifting the car rect in the intended direction
  - Check if the simulated position collides with any obstacle
  - If blocked: suppress the command and trigger a shake sequence
  - If clear: send the movement command to the ESP32 via HTTP
  - If no input: send /stop

The ESP32 is a dumb executor — it only receives /forward, /left, /right,
/backward, /stop.  All decision-making lives here on the laptop.
"""

import time
import threading
import pygame
import requests
from config import (
    ESP32_BASE_URL, ESP32_TIMEOUT, ESP32_ROUTES,
    ENABLE_ESP32, MOVE_SIMULATION_STEP,
    SHAKE_DURATION_FRAMES, SHAKE_INTERVAL_FRAMES,
)


class CarController:
    """
    Reads keyboard state, simulates movement, checks collisions,
    and sends commands to the ESP32.
    """

    def __init__(self):
        # The command we *want* to send this frame
        self.current_command = "stop"

        # The command that was actually sent (after collision check)
        self.active_command = "stop"

        # Whether the current command was blocked by an obstacle
        self.is_blocked = False

        # Shake state
        self._shake_counter = 0
        self._shake_toggle = False  # alternates left/right

        # Track the last command sent to avoid spamming identical requests
        self._last_sent = None

        # Direction → pixel offset for simulating movement
        self._direction_offsets = {
            "forward":  (0, -MOVE_SIMULATION_STEP),
            "backward": (0,  MOVE_SIMULATION_STEP),
            "left":     (-MOVE_SIMULATION_STEP, 0),
            "right":    (MOVE_SIMULATION_STEP,  0),
            "stop":     (0, 0),
        }

    # ------------------------------------------------------------------
    # 1. Read keyboard input
    # ------------------------------------------------------------------

    def read_input(self):
        """
        Sample the current keyboard state and set self.current_command.
        Call once per frame, after pygame.event.get().
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.current_command = "forward"
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.current_command = "backward"
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.current_command = "left"
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.current_command = "right"
        else:
            self.current_command = "stop"

    # ------------------------------------------------------------------
    # 2. Simulate + decide
    # ------------------------------------------------------------------

    def update(self, car_pos, car_size, obstacles):
        """
        Decide what command to actually execute.

        Args:
            car_pos:    [x, y] current car center in game space (or None)
            car_size:   (w, h) car bounding box (or None)
            obstacles:  list of pygame.Rect

        After calling this:
            self.active_command  — the command that should be sent
            self.is_blocked      — True if movement was suppressed
        """
        command = self.current_command

        # If car isn't tracked or no movement requested, just stop
        if car_pos is None or command == "stop":
            self.is_blocked = False
            self.active_command = "stop"
            self._shake_counter = 0
            self._send(self.active_command)
            return

        # Build the current car rect
        w, h = car_size if car_size else (20, 20)
        car_rect = pygame.Rect(
            car_pos[0] - w // 2,
            car_pos[1] - h // 2,
            w, h,
        )

        # Simulate: shift the rect in the intended direction
        dx, dy = self._direction_offsets.get(command, (0, 0))
        simulated = car_rect.move(dx, dy)

        # Check collision with every obstacle
        blocked = any(simulated.colliderect(obs) for obs in obstacles)

        if blocked:
            self.is_blocked = True
            self.active_command = "stop"
            self._do_shake()
        else:
            self.is_blocked = False
            self.active_command = command
            self._shake_counter = 0
            self._send(self.active_command)

    # ------------------------------------------------------------------
    # 3. Shake behavior (blocked)
    # ------------------------------------------------------------------

    def _do_shake(self):
        """
        When blocked, alternate between left and right commands rapidly
        to create a physical "shake" on the car, signaling it can't move.
        """
        self._shake_counter += 1

        if self._shake_counter > SHAKE_DURATION_FRAMES:
            # Shake burst finished — just stop
            self._send("stop")
            self._shake_counter = 0
            return

        # Toggle direction every SHAKE_INTERVAL_FRAMES
        if self._shake_counter % SHAKE_INTERVAL_FRAMES == 0:
            self._shake_toggle = not self._shake_toggle

        shake_cmd = "left" if self._shake_toggle else "right"
        self._send(shake_cmd)

    # ------------------------------------------------------------------
    # 4. Network — send command to ESP32
    # ------------------------------------------------------------------

    def _send(self, command):
        """
        Send a command to the ESP32 via HTTP.
        Uses a fire-and-forget thread so the game loop never blocks.
        Always sends — no duplicate suppression, because many ESP32
        firmwares need continuous requests to keep moving.
        """
        if not ENABLE_ESP32:
            return

        self._last_sent = command
        route = ESP32_ROUTES.get(command, "/stop")
        url = ESP32_BASE_URL + route

        # Fire-and-forget in a daemon thread
        t = threading.Thread(target=self._http_get, args=(url,), daemon=True)
        t.start()

    @staticmethod
    def _http_get(url):
        """Perform a short-timeout GET request. Logs errors for debugging."""
        try:
            r = requests.get(url, timeout=ESP32_TIMEOUT)
            print(f"[ESP32] {url} → {r.status_code}")
        except requests.exceptions.ConnectTimeout:
            print(f"[ESP32] TIMEOUT: {url}")
        except requests.exceptions.ConnectionError:
            print(f"[ESP32] CONNECTION REFUSED: {url}")
        except Exception as e:
            print(f"[ESP32] ERROR: {url} → {e}")
