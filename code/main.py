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
from config import FPS
from tracking import Tracker
from mapping import ProjectionMapper
from game import GameState
from render import Renderer


def main():
    # --- Initialise subsystems ---
    tracker = Tracker()
    mapper = ProjectionMapper()
    game = GameState()
    renderer = Renderer()

    mode = "calibrate"  # "calibrate" or "track"

    # --- OpenCV projection window + mouse callback ---
    cv2.namedWindow("Projection", cv2.WINDOW_NORMAL)

    def _mouse_cb(event, x, y, flags, param):
        if mode == "calibrate":
            mapper.handle_mouse(event, x, y)

    cv2.setMouseCallback("Projection", _mouse_cb)

    # Optional: uncomment for fullscreen projector output
    # cv2.setWindowProperty("Projection", cv2.WND_PROP_FULLSCREEN,
    #                       cv2.WINDOW_FULLSCREEN)

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

        # --- Game logic (only in track mode) ---
        if mode == "track":
            if goal_cooldown > 0:
                goal_cooldown -= 1
            else:
                reached = game.update(result.car_pos, result.car_size)
                if reached:
                    game.advance_level()
                    goal_cooldown = 30  # brief pause before next level activates

        # --- Render game surface ---
        renderer.clear()
        renderer.draw_border()
        renderer.draw_obstacles(game)
        renderer.draw_goal(game.goal_rect)
        renderer.draw_car(result.car_pos, result.car_polygon, result.car_size)
        renderer.draw_debug_corners(result.markers, result.homography)
        renderer.draw_hud(game, mode, result.car_detected)
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
