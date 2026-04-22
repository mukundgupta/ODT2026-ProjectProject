"""
render.py — Pygame rendering for the game surface.

Responsibilities:
  - Draw obstacles (colored by state)
  - Draw the goal area
  - Draw the car (polygon + bounding rect)
  - Draw debug overlays (corner markers, HUD text)
  - Provide the raw Pygame surface for projection warping

Designed for extensibility:
  - FUTURE: add particle effects, animations, sprite-based car
"""

import pygame
import numpy as np
import cv2
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    COLOR_BACKGROUND, COLOR_BORDER, COLOR_CAR,
    COLOR_GOAL, COLOR_GOAL_BORDER, COLOR_DEBUG_CORNER,
)


class Renderer:
    """Draws the game world onto a Pygame surface."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("ArUco Projection Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 20)

    def clear(self, background=None):
        """Fill the screen with the background image or solid color."""
        if background is not None:
            self.screen.blit(background, (0, 0))
        else:
            self.screen.fill(COLOR_BACKGROUND)

    def draw_border(self):
        """Draw a white border around the play area."""
        pygame.draw.rect(
            self.screen, COLOR_BORDER,
            (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 3,
        )

    def draw_obstacles(self, game_state):
        """
        Draw all obstacles as translucent rectangles.
        Color reflects interaction state (normal/near/collision).
        Opacity is controlled by game.OBSTACLE_ALPHA.
        """
        from game import OBSTACLE_ALPHA

        for i, obs in enumerate(game_state.obstacles):
            color = game_state.get_obstacle_color(i)

            # Create a per-obstacle surface with alpha
            surf = pygame.Surface((obs.width, obs.height), pygame.SRCALPHA)
            surf.fill((*color, OBSTACLE_ALPHA))
            self.screen.blit(surf, (obs.x, obs.y))

            # Draw a thin border so the outline is always visible
            pygame.draw.rect(self.screen, color, obs, 2)

    def draw_goal(self, goal_rect):
        """Draw the goal area as a filled rectangle with a border."""
        if goal_rect is None:
            return
        pygame.draw.rect(self.screen, COLOR_GOAL, goal_rect)
        pygame.draw.rect(self.screen, COLOR_GOAL_BORDER, goal_rect, 3)

        # Label
        label = self.font.render("GOAL", True, (0, 0, 0))
        lx = goal_rect.centerx - label.get_width() // 2
        ly = goal_rect.centery - label.get_height() // 2
        self.screen.blit(label, (lx, ly))

    def draw_car(self, car_pos, car_polygon=None, car_size=None):
        """
        Draw the car.
        - If polygon available: draw the mapped marker outline
        - If size available: draw a bounding rect
        - Fallback: draw a circle at car_pos
        """
        if car_pos is None:
            # Car marker not visible at all — nothing to draw
            return

        if car_polygon:
            # Full tracking with homography — draw mapped marker outline
            pygame.draw.polygon(self.screen, COLOR_CAR, car_polygon, 2)

        if car_size:
            # Draw bounding rect around the car
            w, h = car_size
            rect = pygame.Rect(
                car_pos[0] - w // 2,
                car_pos[1] - h // 2,
                w, h,
            )
            pygame.draw.rect(self.screen, COLOR_CAR, rect, 2)
        else:
            # Fallback: no homography, but car marker is detected.
            # Draw a simple dot at the estimated position.
            pygame.draw.circle(self.screen, COLOR_CAR, car_pos, 10)

    def draw_debug_corners(self, markers, homography):
        """
        Draw the 4 corner markers mapped into game space.
        Useful for verifying calibration.
        """
        if homography is None:
            return

        from config import CORNER_IDS

        for mid in CORNER_IDS:
            if mid in markers:
                pt = np.array([[markers[mid]]], dtype=np.float32)
                mapped = cv2.perspectiveTransform(pt, homography)
                x, y = mapped[0][0]
                pygame.draw.circle(
                    self.screen, COLOR_DEBUG_CORNER,
                    (int(x), int(y)), 8,
                )

    def draw_hud(self, game_state, mode, car_detected, controller=None):
        """Draw a small heads-up display with level info, mode, and controls."""
        lines = [
            f"Mode: {mode.upper()}",
            f"{game_state.level_name}",
        ]
        if game_state.game_complete:
            lines.append("ALL LEVELS COMPLETE — looping")
        if not car_detected:
            lines.append("Car: NOT DETECTED")

        # Show controller state when available
        if controller is not None:
            cmd = controller.active_command.upper()
            if controller.is_blocked:
                lines.append(f"Command: {controller.current_command.upper()} → BLOCKED")
            else:
                lines.append(f"Command: {cmd}")

        y = 10
        for line in lines:
            surf = self.font.render(line, True, (200, 200, 200))
            self.screen.blit(surf, (10, y))
            y += 24

    def draw_transition(self, transition):
        """Draw the level transition overlay (fade + title text)."""
        if transition.active:
            transition.draw(self.screen)

    def flip(self):
        """Update the display."""
        pygame.display.flip()

    def tick(self, fps):
        """Limit frame rate and return delta time."""
        return self.clock.tick(fps)

    def get_surface(self):
        """Return the current Pygame display surface (for warping)."""
        return self.screen

    def quit(self):
        """Shut down Pygame."""
        pygame.quit()
