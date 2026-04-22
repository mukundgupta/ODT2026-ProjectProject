"""
mapping.py — Coordinate transforms and projection warp.

Responsibilities:
  - Manage the 4 draggable projection-calibration points
  - Compute the Pygame-surface → projector perspective transform
  - Warp a Pygame surface for projector output
  - Handle mouse interaction for calibration dragging
"""

import cv2
import numpy as np
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT,
    CALIBRATION_POINT_RADIUS, DEFAULT_DST_POINTS,
    COLOR_CALIBRATION_POINT, COLOR_CALIBRATION_TEXT,
)


class ProjectionMapper:
    """Handles perspective warp from game surface to projector output."""

    def __init__(self):
        # Source corners = full game surface
        self.src_pts = np.float32([
            [0, 0],
            [SCREEN_WIDTH, 0],
            [SCREEN_WIDTH, SCREEN_HEIGHT],
            [0, SCREEN_HEIGHT],
        ])

        # Destination corners (editable during calibration)
        self.dst_pts = np.float32([list(p) for p in DEFAULT_DST_POINTS])

        # Drag state
        self._selected = None

    # ------------------------------------------------------------------
    # Calibration interaction
    # ------------------------------------------------------------------

    def handle_mouse(self, event, x, y):
        """
        Process an OpenCV mouse event for dragging calibration points.
        Call this from the cv2 mouse callback.
        """
        r = CALIBRATION_POINT_RADIUS

        if event == cv2.EVENT_LBUTTONDOWN:
            for i, pt in enumerate(self.dst_pts):
                if np.linalg.norm(pt - [x, y]) < r:
                    self._selected = i
                    break

        elif event == cv2.EVENT_MOUSEMOVE:
            if self._selected is not None:
                self.dst_pts[self._selected] = [x, y]

        elif event == cv2.EVENT_LBUTTONUP:
            self._selected = None

    # ------------------------------------------------------------------
    # Warp
    # ------------------------------------------------------------------

    def warp(self, pygame_surface):
        """
        Convert a Pygame surface to a warped OpenCV image for the projector.

        Returns a BGR numpy array ready for cv2.imshow().
        """
        import pygame  # local import to avoid top-level Pygame dependency

        # Pygame surface → numpy
        arr = pygame.surfarray.array3d(pygame_surface)
        arr = np.transpose(arr, (1, 0, 2))
        frame = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)

        # Perspective warp
        H = cv2.getPerspectiveTransform(self.src_pts, self.dst_pts)
        warped = cv2.warpPerspective(frame, H, (SCREEN_WIDTH, SCREEN_HEIGHT))
        return warped

    def draw_calibration_points(self, warped_image):
        """
        Draw the draggable corner handles onto the warped image.
        Only shown during calibration mode.
        """
        r = CALIBRATION_POINT_RADIUS
        for i, pt in enumerate(self.dst_pts):
            pt_int = tuple(pt.astype(int))
            cv2.circle(warped_image, pt_int, r, COLOR_CALIBRATION_POINT, -1)
            cv2.putText(
                warped_image, str(i), pt_int,
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, COLOR_CALIBRATION_TEXT, 2,
            )
