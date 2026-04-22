"""
config.py — Central configuration for the ArUco projection game.

All constants, IDs, sizes, and tuning values live here.
Adjust these to match your physical setup.
"""

# =============================================================================
# Display
# =============================================================================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# =============================================================================
# Camera
# =============================================================================
CAMERA_INDEX = 0
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720
CAMERA_FPS = 60
CAMERA_EXPOSURE = -6
CAMERA_GAIN = 0

# =============================================================================
# ArUco
# =============================================================================
ARUCO_DICT_TYPE = "DICT_6X6_250"

# Corner marker IDs (define the play-field boundary)
CORNER_IDS = [1, 2, 3, 4]

# Mapping: corner marker ID → game-space corner
# Order: top-left, top-right, bottom-right, bottom-left
CORNER_ID_ORDER = [3, 4, 2, 1]

# Car marker ID
CAR_MARKER_ID = 42

# =============================================================================
# Tracking / Smoothing
# =============================================================================
# Exponential smoothing factor (0 = no smoothing, 1 = full lag)
SMOOTHING_FACTOR = 0.7

# Maximum pixel jump per frame (clamps noisy spikes)
MAX_STEP = 40

# Default car position when not yet detected
DEFAULT_CAR_POS = [400, 300]

# =============================================================================
# Projection Calibration
# =============================================================================
# Draggable-point hit radius (pixels)
CALIBRATION_POINT_RADIUS = 15

# Default projector destination corners
DEFAULT_DST_POINTS = [
    [100, 50],
    [700, 0],
    [750, 550],
    [50, 600],
]

# =============================================================================
# Game — Obstacle proximity
# =============================================================================
# Inflate amount (px) for the "near" buffer zone around obstacles
PROXIMITY_BUFFER = 25

# =============================================================================
# Colors (R, G, B for Pygame)
# =============================================================================
COLOR_BACKGROUND = (0, 0, 0)
COLOR_BORDER = (255, 255, 255)
COLOR_OBSTACLE_NORMAL = (255, 0, 0)
COLOR_OBSTACLE_NEAR = (255, 165, 0)
COLOR_OBSTACLE_COLLISION = (0, 0, 255)
COLOR_CAR = (0, 255, 0)
COLOR_GOAL = (0, 255, 200)
COLOR_GOAL_BORDER = (0, 200, 150)
COLOR_DEBUG_CORNER = (0, 0, 255)
COLOR_CALIBRATION_POINT = (0, 255, 255)  # BGR in OpenCV context
COLOR_CALIBRATION_TEXT = (0, 0, 255)

# =============================================================================
# Future hooks — placeholder flags
# =============================================================================
# Set True when ESP32 integration is ready
ENABLE_ESP32 = False
# Set True when phone/controller input is ready
ENABLE_REMOTE_INPUT = False
# Set True when sound effects are ready
ENABLE_SOUND = False
