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
# Which monitor to use for the projector (0 = primary, 1 = second display)
PROJECTOR_MONITOR = 1

# Draggable-point hit radius (pixels)
CALIBRATION_POINT_RADIUS = 15

# Default projector destination corners (moved inward for visibility)
DEFAULT_DST_POINTS = [
    [200, 150],
    [600, 150],
    [600, 450],
    [200, 450],
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
# ESP32 Control
# =============================================================================
ESP32_IP = "192.168.4.1"
ESP32_BASE_URL = f"http://{ESP32_IP}"
ESP32_TIMEOUT = 0.15  # seconds — short enough to not block, long enough for WiFi

# How many pixels to shift the car rect when simulating a move
MOVE_SIMULATION_STEP = 30

# Shake behavior: alternates left/right when blocked
SHAKE_DURATION_FRAMES = 6   # total frames per shake burst
SHAKE_INTERVAL_FRAMES = 3   # frames between left/right toggle

# Command routes (appended to ESP32_BASE_URL)
ESP32_ROUTES = {
    "forward":  "/forward",
    "backward": "/backward",
    "left":     "/left",
    "right":    "/right",
    "stop":     "/stop",
}

# =============================================================================
# Future hooks — placeholder flags
# =============================================================================
# Set True when ESP32 integration is ready
ENABLE_ESP32 = True
# Set True when phone/controller input is ready
ENABLE_REMOTE_INPUT = False
# Set True when sound effects are ready
ENABLE_SOUND = False
