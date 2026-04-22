"""
tracking.py — ArUco detection, homography, and smoothed car tracking.

Responsibilities:
  - Open and read the camera
  - Detect ArUco markers each frame
  - Compute camera → game-space homography from corner markers
  - Track the car marker with exponential smoothing + jump clamping
  - Return structured tracking data for the game loop
"""

import cv2
import numpy as np
from config import (
    CAMERA_INDEX, CAMERA_WIDTH, CAMERA_HEIGHT, CAMERA_FPS,
    CAMERA_EXPOSURE, CAMERA_GAIN,
    ARUCO_DICT_TYPE, CORNER_IDS, CORNER_ID_ORDER, CAR_MARKER_ID,
    SMOOTHING_FACTOR, MAX_STEP, DEFAULT_CAR_POS,
    SCREEN_WIDTH, SCREEN_HEIGHT,
)


class Tracker:
    """Handles camera capture, ArUco detection, and car position tracking."""

    def __init__(self):
        # Camera
        self.cap = cv2.VideoCapture(CAMERA_INDEX)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, CAMERA_FPS)
        self.cap.set(cv2.CAP_PROP_EXPOSURE, CAMERA_EXPOSURE)
        self.cap.set(cv2.CAP_PROP_GAIN, CAMERA_GAIN)

        # ArUco detector
        dict_id = getattr(cv2.aruco, ARUCO_DICT_TYPE)
        aruco_dict = cv2.aruco.getPredefinedDictionary(dict_id)
        params = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(aruco_dict, params)

        # Smoothing state
        self._prev_pos = list(DEFAULT_CAR_POS)

        # Game-space corners (match CORNER_ID_ORDER)
        self._game_corners = np.float32([
            [0, 0],
            [SCREEN_WIDTH, 0],
            [SCREEN_WIDTH, SCREEN_HEIGHT],
            [0, SCREEN_HEIGHT],
        ])

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def read_frame(self):
        """Grab a camera frame. Returns (success, frame)."""
        return self.cap.read()

    def detect(self, frame):
        """
        Run full detection pipeline on a BGR frame.

        Returns a TrackingResult with all relevant data.
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = self.detector.detectMarkers(gray)

        result = TrackingResult()

        if ids is None:
            return result

        ids_flat = ids.flatten()

        # Build marker center lookup
        for i, marker_id in enumerate(ids_flat):
            c = corners[i][0]
            center = c.mean(axis=0)
            result.markers[int(marker_id)] = center

        # Check if all 4 corner markers are visible
        if all(cid in result.markers for cid in CORNER_IDS):
            cam_pts = np.float32([result.markers[cid] for cid in CORNER_ID_ORDER])
            result.homography = cv2.getPerspectiveTransform(cam_pts, self._game_corners)

        # Track car marker
        if CAR_MARKER_ID in ids_flat:
            idx = list(ids_flat).index(CAR_MARKER_ID)
            car_corners = corners[idx][0]  # 4 corner points

            if result.homography is not None:
                # Full tracking: map corners into game space via homography
                pts = np.array([car_corners], dtype=np.float32)
                mapped = cv2.perspectiveTransform(pts, result.homography)[0]

                raw_x = float(mapped[:, 0].mean())
                raw_y = float(mapped[:, 1].mean())

                # Bounding box from mapped corners
                xs = [p[0] for p in mapped]
                ys = [p[1] for p in mapped]
                w = int(max(xs) - min(xs))
                h = int(max(ys) - min(ys))
                result.car_size = (w, h)

                # Polygon (raw mapped corners, useful for drawing)
                result.car_polygon = [(int(p[0]), int(p[1])) for p in mapped]
            else:
                # Fallback: no corner markers visible, so scale the raw
                # camera-pixel center into game space using simple ratio.
                # Not accurate, but keeps the car dot visible on screen.
                cam_center = car_corners.mean(axis=0)
                raw_x = float(cam_center[0] / CAMERA_WIDTH * SCREEN_WIDTH)
                raw_y = float(cam_center[1] / CAMERA_HEIGHT * SCREEN_HEIGHT)

            # Clamp jump
            dx = max(-MAX_STEP, min(MAX_STEP, raw_x - self._prev_pos[0]))
            dy = max(-MAX_STEP, min(MAX_STEP, raw_y - self._prev_pos[1]))
            limited_x = self._prev_pos[0] + dx
            limited_y = self._prev_pos[1] + dy

            # Exponential smoothing
            s = SMOOTHING_FACTOR
            smooth_x = int(s * self._prev_pos[0] + (1 - s) * limited_x)
            smooth_y = int(s * self._prev_pos[1] + (1 - s) * limited_y)

            result.car_pos = [smooth_x, smooth_y]
            self._prev_pos = result.car_pos.copy()
            result.car_detected = True

        return result

    def release(self):
        """Release the camera."""
        self.cap.release()


class TrackingResult:
    """Container for one frame's tracking output."""

    def __init__(self):
        self.markers = {}          # {marker_id: np.array([x, y])}
        self.homography = None     # 3×3 camera→game transform (or None)
        self.car_pos = None        # [x, y] smoothed game-space center
        self.car_size = None       # (w, h) bounding box in game space
        self.car_polygon = None    # [(x,y), ...] 4 mapped corners
        self.car_detected = False  # True when car marker is visible
