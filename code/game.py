"""
game.py — Game logic: levels, obstacles, goals, collision, and rules.

Responsibilities:
  - Define level data (obstacles + goal area)
  - Manage level progression
  - Detect collision and proximity between car and obstacles
  - Detect goal completion
  - Provide state for the renderer

Designed for extensibility:
  - Add new levels by appending to LEVELS
  - Hook points marked with "# FUTURE:" comments for ESP32, sound, etc.
"""

import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PROXIMITY_BUFFER,
    COLOR_OBSTACLE_NORMAL, COLOR_OBSTACLE_NEAR, COLOR_OBSTACLE_COLLISION,
)


# =============================================================================
# Level definitions
# =============================================================================
# Each level is a dict with:
#   "obstacles" : list of (x, y, w, h) tuples
#   "goal"      : (x, y, w, h) rectangle the car must reach

LEVELS = [
    {
        "name": "Level 1 — Straight Run",
        "obstacles": [
            (200, 150, 200, 100),
            (500, 350, 100, 150),
        ],
        "goal": (680, 480, 100, 100),
    },
    {
        "name": "Level 2 — Narrow Corridor",
        "obstacles": [
            (150, 0, 80, 350),
            (150, 450, 80, 150),
            (400, 100, 80, 350),
            (400, 0, 300, 60),
        ],
        "goal": (600, 250, 100, 100),
    },
    {
        "name": "Level 3 — Maze",
        "obstacles": [
            (100, 100, 250, 40),
            (100, 100, 40, 300),
            (300, 250, 40, 200),
            (450, 50, 40, 250),
            (500, 350, 200, 40),
        ],
        "goal": (650, 50, 100, 100),
    },
]


class GameState:
    """Manages the active level, obstacle interaction, and goal detection."""

    def __init__(self):
        self.current_level_index = 0
        self.obstacles = []        # list of pygame.Rect
        self.goal_rect = None      # pygame.Rect
        self.level_name = ""
        self.game_complete = False  # True after all levels finished

        # Per-obstacle state for rendering
        # Maps obstacle index → "normal" | "near" | "collision"
        self.obstacle_states = {}

        self._load_level(self.current_level_index)

    # ------------------------------------------------------------------
    # Level management
    # ------------------------------------------------------------------

    def _load_level(self, index):
        """Load a level by index."""
        if index >= len(LEVELS):
            self.game_complete = True
            print("[GAME] All levels complete!")
            # FUTURE: trigger victory animation / sound
            return

        level = LEVELS[index]
        self.level_name = level["name"]
        self.obstacles = [pygame.Rect(*o) for o in level["obstacles"]]
        gx, gy, gw, gh = level["goal"]
        self.goal_rect = pygame.Rect(gx, gy, gw, gh)
        self.obstacle_states = {i: "normal" for i in range(len(self.obstacles))}
        self.game_complete = False

        print(f"[GAME] Loaded: {self.level_name}")
        # FUTURE: play level-start sound

    def advance_level(self):
        """Move to the next level, or loop back to the first."""
        self.current_level_index += 1
        if self.current_level_index >= len(LEVELS):
            # Loop back to level 1
            print("[GAME] Looping back to Level 1")
            self.current_level_index = 0
        self._load_level(self.current_level_index)

    def reset(self):
        """Restart from level 1."""
        self.current_level_index = 0
        self._load_level(0)

    # ------------------------------------------------------------------
    # Per-frame update
    # ------------------------------------------------------------------

    def update(self, car_pos, car_size=None):
        """
        Update game state for the current frame.

        Args:
            car_pos:  [x, y] in game space (or None if car not detected)
            car_size: (w, h) bounding box of the car (or None)

        Returns:
            True if the car reached the goal this frame.
        """
        if car_pos is None or self.game_complete:
            return False

        # Build a rect for the car (fallback to a small square)
        if car_size:
            w, h = car_size
        else:
            w, h = 20, 20
        car_rect = pygame.Rect(
            car_pos[0] - w // 2,
            car_pos[1] - h // 2,
            w, h,
        )

        # --- Obstacle interaction ---
        any_collision = False
        for i, obs in enumerate(self.obstacles):
            expanded = obs.inflate(PROXIMITY_BUFFER, PROXIMITY_BUFFER)

            if obs.colliderect(car_rect):
                self.obstacle_states[i] = "collision"
                any_collision = True
                # FUTURE: send stop signal to ESP32
                # FUTURE: play collision sound
                # FUTURE: trigger obstacle shake animation
            elif expanded.colliderect(car_rect):
                self.obstacle_states[i] = "near"
                # FUTURE: send slow-down signal to ESP32
            else:
                self.obstacle_states[i] = "normal"

        # --- Goal detection ---
        if self.goal_rect and self.goal_rect.colliderect(car_rect):
            if not any_collision:
                print(f"[GAME] Goal reached! ({self.level_name})")
                # FUTURE: play goal sound
                return True

        return False

    # ------------------------------------------------------------------
    # Helpers for renderer
    # ------------------------------------------------------------------

    def get_obstacle_color(self, index):
        """Return the Pygame color for an obstacle based on its state."""
        state = self.obstacle_states.get(index, "normal")
        if state == "collision":
            return COLOR_OBSTACLE_COLLISION
        elif state == "near":
            return COLOR_OBSTACLE_NEAR
        return COLOR_OBSTACLE_NORMAL
