"""
game.py — Game logic: levels, obstacles, goals, collision, and rules.

Responsibilities:
  - Define level data (obstacles, goal area, background image)
  - Convert 12×12 grid coordinates to pixel coordinates
  - Manage level progression with transition animations
  - Detect collision and proximity between car and obstacles
  - Detect goal completion
  - Provide state for the renderer
"""

import os
import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    PROXIMITY_BUFFER,
    COLOR_OBSTACLE_NORMAL, COLOR_OBSTACLE_NEAR, COLOR_OBSTACLE_COLLISION,
)


# =============================================================================
# Grid system — 12×12 grid mapped to SCREEN_WIDTH × SCREEN_HEIGHT
# =============================================================================
GRID_COLS = 12
GRID_ROWS = 12
CELL_W = SCREEN_WIDTH / GRID_COLS    # ~66.67 px
CELL_H = SCREEN_HEIGHT / GRID_ROWS   # 50 px


def grid_rect(col, row, cols_wide=1, rows_tall=1):
    """
    Convert grid coordinates to a pixel (x, y, w, h) tuple.

    Grid origin (1,1) is at the BOTTOM-RIGHT of the screen.
    Column numbers increase leftward, row numbers increase upward.

    Args:
        col:        1-based column (1 = rightmost)
        row:        1-based row (1 = bottom)
        cols_wide:  width in grid cells
        rows_tall:  height in grid cells

    Returns:
        (x, y, w, h) in pixel coordinates
    """
    w = int(cols_wide * CELL_W)
    h = int(rows_tall * CELL_H)
    # Columns go left-to-right (col 1 = left edge)
    # Rows are flipped: row 1 = bottom edge
    x = int((col - 1) * CELL_W)
    y = int(SCREEN_HEIGHT - (row - 1) * CELL_H - h)
    return (x, y, w, h)


# =============================================================================
# Level definitions
# =============================================================================
# Obstacles and goals are defined in grid coordinates using grid_rect().
# grid_rect(col, row, width_in_cells, height_in_cells)

LEVELS = [
    {
        "name": "Level 1 — Earth",
        "background": os.path.join("maps", "earth-map.jpeg"),
        "obstacles": [
            grid_rect(6, 2, 1, 4),     # 1×4 at (6,2)
            grid_rect(9, 5, 4, 3),     # 4×3 at (9,5)
            grid_rect(4, 7, 2, 4),     # 2×4 at (4,7)
            grid_rect(6, 10, 4, 1),    # 4×1 at (6,10)
            grid_rect(1, 3, 1, 9),     # 1×9 at (1,3)
            grid_rect(2, 4, 2, 1),     # 2×1 at (2,4)
        ],
        "goal": grid_rect(2, 2, 2, 2),
    },
    {
        "name": "Level 2 — Water",
        "background": os.path.join("maps", "water-map.jpeg"),
        "obstacles": [
            grid_rect(5, 1, 7, 3),     # origin (5,1), 7 wide × 3 tall
            grid_rect(2, 7, 2, 2),     # origin (2,7), 2×2
            grid_rect(8, 9, 3, 2),     # origin (8,9), 3 wide × 2 tall
        ],
        "goal": grid_rect(11, 11, 2, 2),
    },
    {
        "name": "Level 3 — Lava",
        "background": os.path.join("maps", "lava-map.jpeg"),
        "obstacles": [
            grid_rect(4, 5, 1, 6),     # 1×6 at (4,5)
            grid_rect(5, 9, 8, 2),     # 8×2 at (5,9)
            grid_rect(7, 3, 3, 3),     # 3×3 at (7,3)
        ],
        "goal": grid_rect(10, 3, 2, 2),
    },
]

# Obstacle drawing opacity (0 = invisible, 255 = solid)
# Set to ~120 for translucent debug view, 0 to hide completely
OBSTACLE_ALPHA = 40


# =============================================================================
# Transition animation
# =============================================================================

class LevelTransition:
    """
    Handles the animated transition between levels.

    Sequence:
      1. Fade to black (fade_out)
      2. Show level name text briefly (title_hold)
      3. Fade in the new level (fade_in)
    """

    # Duration in frames for each phase
    FADE_OUT_FRAMES = 30
    TITLE_HOLD_FRAMES = 60
    FADE_IN_FRAMES = 30

    def __init__(self):
        self.active = False
        self.phase = None          # "fade_out", "title_hold", "fade_in"
        self.frame_counter = 0
        self.level_name = ""
        self._overlay = None       # pre-built black surface for fading

    def start(self, level_name):
        """Begin a transition to a new level."""
        self.active = True
        self.phase = "fade_out"
        self.frame_counter = 0
        self.level_name = level_name

        # Build a black overlay surface once
        if self._overlay is None:
            self._overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            self._overlay.fill((0, 0, 0))

    def tick(self):
        """
        Advance the transition by one frame.
        Returns True when the transition is fully complete.
        """
        if not self.active:
            return False

        self.frame_counter += 1

        if self.phase == "fade_out":
            if self.frame_counter >= self.FADE_OUT_FRAMES:
                self.phase = "title_hold"
                self.frame_counter = 0

        elif self.phase == "title_hold":
            if self.frame_counter >= self.TITLE_HOLD_FRAMES:
                self.phase = "fade_in"
                self.frame_counter = 0

        elif self.phase == "fade_in":
            if self.frame_counter >= self.FADE_IN_FRAMES:
                self.active = False
                self.phase = None
                self.frame_counter = 0
                return True  # transition complete

        return False

    def get_alpha(self):
        """
        Return the overlay alpha (0–255) for the current frame.
        0 = fully transparent (game visible), 255 = fully black.
        """
        if self.phase == "fade_out":
            # Ramp from 0 → 255
            progress = self.frame_counter / max(self.FADE_OUT_FRAMES, 1)
            return int(255 * progress)

        elif self.phase == "title_hold":
            return 255

        elif self.phase == "fade_in":
            # Ramp from 255 → 0
            progress = self.frame_counter / max(self.FADE_IN_FRAMES, 1)
            return int(255 * (1.0 - progress))

        return 0

    def draw(self, screen):
        """Draw the transition overlay and title text onto the screen."""
        if not self.active:
            return

        alpha = self.get_alpha()
        self._overlay.set_alpha(alpha)
        screen.blit(self._overlay, (0, 0))

        # Show level name during title hold and early fade-in
        if self.phase in ("title_hold", "fade_in"):
            font = pygame.font.SysFont("monospace", 48, bold=True)
            text_surf = font.render(self.level_name, True, (255, 255, 255))
            text_surf.set_alpha(alpha if self.phase == "fade_in" else 255)
            x = SCREEN_WIDTH // 2 - text_surf.get_width() // 2
            y = SCREEN_HEIGHT // 2 - text_surf.get_height() // 2
            screen.blit(text_surf, (x, y))


# =============================================================================
# Game state
# =============================================================================

class GameState:
    """Manages the active level, obstacle interaction, and goal detection."""

    def __init__(self):
        self.current_level_index = 0
        self.obstacles = []        # list of pygame.Rect
        self.goal_rect = None      # pygame.Rect
        self.level_name = ""
        self.game_complete = False
        self.background = None     # pygame.Surface (scaled map image)

        # Per-obstacle state for rendering
        self.obstacle_states = {}

        # Transition animation
        self.transition = LevelTransition()
        self._pending_level = None  # level index to load after fade-out

        self._load_level(self.current_level_index)

    # ------------------------------------------------------------------
    # Level management
    # ------------------------------------------------------------------

    def _load_level(self, index):
        """Load a level by index."""
        if index >= len(LEVELS):
            self.game_complete = True
            print("[GAME] All levels complete!")
            return

        level = LEVELS[index]
        self.level_name = level["name"]
        self.obstacles = [pygame.Rect(*o) for o in level["obstacles"]]
        gx, gy, gw, gh = level["goal"]
        self.goal_rect = pygame.Rect(gx, gy, gw, gh)
        self.obstacle_states = {i: "normal" for i in range(len(self.obstacles))}
        self.game_complete = False

        # Load and scale background image
        bg_path = level.get("background")
        if bg_path and os.path.exists(bg_path):
            raw = pygame.image.load(bg_path).convert()
            self.background = pygame.transform.scale(raw, (SCREEN_WIDTH, SCREEN_HEIGHT))
            print(f"[GAME] Loaded background: {bg_path}")
        else:
            self.background = None
            if bg_path:
                print(f"[GAME] WARNING: background not found: {bg_path}")

        print(f"[GAME] Loaded: {self.level_name}")

    def advance_level(self):
        """Start a transition to the next level."""
        next_index = self.current_level_index + 1
        if next_index >= len(LEVELS):
            next_index = 0
            print("[GAME] Looping back to Level 1")

        # Don't load yet — start the transition animation first
        self._pending_level = next_index
        next_name = LEVELS[next_index]["name"]
        self.transition.start(next_name)

    def reset(self):
        """Restart from level 1 (immediate, no transition)."""
        self.current_level_index = 0
        self._pending_level = None
        self.transition.active = False
        self._load_level(0)

    # ------------------------------------------------------------------
    # Per-frame update
    # ------------------------------------------------------------------

    def update(self, car_pos, car_size=None):
        """
        Update game state for the current frame.

        Returns True if the car reached the goal this frame.
        """
        # If a transition is playing, advance it
        if self.transition.active:
            finished = self.transition.tick()

            # Load the new level at the midpoint (when screen is black)
            if self.transition.phase == "title_hold" and self.transition.frame_counter == 1:
                if self._pending_level is not None:
                    self.current_level_index = self._pending_level
                    self._load_level(self._pending_level)
                    self._pending_level = None

            return False  # don't process game logic during transitions

        if car_pos is None or self.game_complete:
            return False

        # Build a rect for the car
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
            elif expanded.colliderect(car_rect):
                self.obstacle_states[i] = "near"
            else:
                self.obstacle_states[i] = "normal"

        # --- Goal detection ---
        if self.goal_rect and self.goal_rect.colliderect(car_rect):
            if not any_collision:
                print(f"[GAME] Goal reached! ({self.level_name})")
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

    def would_collide(self, rect):
        """Check if a pygame.Rect overlaps any obstacle. Used by controller."""
        return any(rect.colliderect(obs) for obs in self.obstacles)
