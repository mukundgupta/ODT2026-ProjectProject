"""
main.py — Entry point for the ArUco projection game.

Modes:
  CALIBRATE  — drag projection corners to align with the physical surface
  TRACK      — full game loop with live car tracking

Controls:
  SPACE  — toggle between calibrate / track mode
  R      — reset to level 1
  ESC    — quit

Architecture:
  main.py  orchestrates the loop
  tracking.py  reads camera + detects markers
  mapping.py   warps the game surface for the projector
  game.py      manages levels, obstacles, goals, collisions
  render.py    draws everything with Pygame
  config.py    central constants
"""

import sys
import cv2
import pygame
from config import FPS, PROJECTOR_MONITOR
from tracking import Tracker
from mapping import ProjectionMapper
from game import GameState
from render import Renderer
from controller import CarController


def main():
    # --- Initialise subsystems ---
    tracker = Tracker()
    mapper = ProjectionMapper()
    renderer = Renderer()       # must init before GameState (needs display for image loading)
    game = GameState()
    controller = CarController()

    mode = "calibrate"  # "calibrate" or "track"

    # --- OpenCV projection window + mouse callback ---
    cv2.namedWindow("Projection", cv2.WINDOW_NORMAL)

    def _mouse_cb(event, x, y, flags, param):
        if mode == "calibrate":
            mapper.handle_mouse(event, x, y)

    cv2.setMouseCallback("Projection", _mouse_cb)

    # Move window to the second display, then go fullscreen.
    # screeninfo gives us the monitor offset so OpenCV places the
    # window on the right screen before expanding it.
    try:
        from screeninfo import get_monitors
        monitors = get_monitors()
        if len(monitors) >= 2:
            m = monitors[PROJECTOR_MONITOR]
            cv2.moveWindow("Projection", m.x, m.y)
            cv2.setWindowProperty("Projection", cv2.WND_PROP_FULLSCREEN,
                                  cv2.WINDOW_FULLSCREEN)
            print(f"[DISPLAY] Fullscreen on monitor {PROJECTOR_MONITOR}: "
                  f"{m.width}x{m.height} at ({m.x},{m.y})")
        else:
            print("[DISPLAY] Only one monitor detected — running windowed")
    except ImportError:
        print("[DISPLAY] screeninfo not installed — running windowed. "
              "Install with: pip install screeninfo")

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------
    running = True
    goal_cooldown = 0  # frames to wait after reaching a goal

    while running:
        # --- Pygame events ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mode = "track" if mode == "calibrate" else "calibrate"
                    print(f"[MODE] Switched to {mode.upper()}")

                elif event.key == pygame.K_r:
                    game.reset()
                    print("[MODE] Game reset to Level 1")

                elif event.key == pygame.K_ESCAPE:
                    running = False

        # --- Camera + detection ---
        ret, frame = tracker.read_frame()
        if not ret:
            continue

        result = tracker.detect(frame)

        # --- Controller: read keyboard + decide command ---
        controller.read_input()

        # --- Game logic (only in track mode) ---
        if mode == "track":
            if goal_cooldown > 0:
                goal_cooldown -= 1
            else:
                reached = game.update(result.car_pos, result.car_size)
                if reached:
                    game.advance_level()
                    goal_cooldown = 30  # brief pause before next level activates

            # Controller: simulate move, check collision, send to ESP32
            # Skip controller during transitions so the car doesn't move
            if not game.transition.active:
                controller.update(result.car_pos, result.car_size, game.obstacles)

        # --- Render game surface ---
        renderer.clear(game.background)
        renderer.draw_border()
        renderer.draw_obstacles(game)
        renderer.draw_goal(game.goal_rect)
        renderer.draw_car(result.car_pos, result.car_polygon, result.car_size)
        renderer.draw_debug_corners(result.markers, result.homography)
        renderer.draw_hud(game, mode, result.car_detected, controller)
        renderer.draw_transition(game.transition)
        renderer.flip()

        # --- Warp for projector ---
        warped = mapper.warp(renderer.get_surface())

        if mode == "calibrate":
            mapper.draw_calibration_points(warped)

        cv2.imshow("Projection", warped)

        # Show raw camera feed for debugging
        cv2.imshow("Camera", frame)

        # --- OpenCV key check (backup ESC) ---
        if cv2.waitKey(1) & 0xFF == 27:
            running = False

        renderer.tick(FPS)

    # --- Cleanup ---
    tracker.release()
    renderer.quit()
    cv2.destroyAllWindows()
    print("[EXIT] Clean shutdown.")


if __name__ == "__main__":
    main()
