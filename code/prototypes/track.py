import pygame
import numpy as np
import cv2

# --- INIT ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# --- CAMERA ---
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 60)
cap.set(cv2.CAP_PROP_EXPOSURE, -6)  # lower = less blur
cap.set(cv2.CAP_PROP_GAIN, 0)
# --- ARUCO ---
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
detector = cv2.aruco.ArucoDetector(aruco_dict, cv2.aruco.DetectorParameters())

# --- SMOOTHING ---
SMOOTHING = 0.7
MAX_STEP = 40

prev_car_pos = [400, 300]

# --- GAME ---
car_pos = [400, 300]
car_rect = None
car_polygon = None

obstacles = [
    pygame.Rect(200, 150, 200, 100),
    pygame.Rect(500, 300, 100, 200)
]

# --- PROJECTOR WARP ---
src_pts = np.float32([
    [0, 0],
    [WIDTH, 0],
    [WIDTH, HEIGHT],
    [0, HEIGHT]
])

dst_pts = np.float32([
    [100, 50],
    [700, 0],
    [750, 550],
    [50, 600]
])

selected_point = None
RADIUS = 15

# --- MODE ---
mode = "calibrate"

# --- MOUSE DRAG ---
def mouse_callback(event, x, y, flags, param):
    global selected_point, dst_pts

    if mode != "calibrate":
        return

    if event == cv2.EVENT_LBUTTONDOWN:
        for i, pt in enumerate(dst_pts):
            if np.linalg.norm(pt - [x, y]) < RADIUS:
                selected_point = i
                break

    elif event == cv2.EVENT_MOUSEMOVE:
        if selected_point is not None:
            dst_pts[selected_point] = [x, y]

    elif event == cv2.EVENT_LBUTTONUP:
        selected_point = None

# --- WINDOW ---
cv2.namedWindow("Projection", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Projection", mouse_callback)

# --- MAIN LOOP ---
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mode = "track"
                print("Switched to TRACK mode")

    # --- CAMERA ---
    ret, frame = cap.read()
    if not ret:
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = detector.detectMarkers(gray)

    marker_dict = {}
    H_cam_to_game = None

    if ids is not None:
        ids = ids.flatten()

        # --- DETECT MARKERS ---
        for i, marker_id in enumerate(ids):
            c = corners[i][0]
            center = c.mean(axis=0)
            marker_dict[marker_id] = center

            center_int = tuple(center.astype(int))

            cv2.circle(frame, center_int, 6, (0, 255, 0), -1)
            cv2.putText(frame, f"ID {marker_id}",
                        (center_int[0]+5, center_int[1]-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

            if marker_id in [1,2,3,4]:
                cv2.circle(frame, center_int, 15, (0, 0, 255), 2)

        # --- HOMOGRAPHY ---
        if all(k in marker_dict for k in [1,2,3,4]):

            cam_pts = np.float32([
                marker_dict[3],
                marker_dict[4],
                marker_dict[2],
                marker_dict[1],
            ])

            game_pts = np.float32([
                [0, 0],
                [WIDTH, 0],
                [WIDTH, HEIGHT],
                [0, HEIGHT],
            ])

            H_cam_to_game = cv2.getPerspectiveTransform(cam_pts, game_pts)

            # --- TRACK CAR ---
            if 42 in ids:
                idx = list(ids).index(42)
                c = corners[idx][0]

                pts = np.array([c], dtype=np.float32)
                mapped = cv2.perspectiveTransform(pts, H_cam_to_game)[0]

                xs = [p[0] for p in mapped]
                ys = [p[1] for p in mapped]

                new_x = int(sum(xs)/4)
                new_y = int(sum(ys)/4)

                # --- LIMIT JUMP ---
                dx = new_x - prev_car_pos[0]
                dy = new_y - prev_car_pos[1]

                dx = max(-MAX_STEP, min(MAX_STEP, dx))
                dy = max(-MAX_STEP, min(MAX_STEP, dy))

                limited_x = prev_car_pos[0] + dx
                limited_y = prev_car_pos[1] + dy

                # --- SMOOTHING ---
                smooth_x = int(SMOOTHING * prev_car_pos[0] + (1 - SMOOTHING) * limited_x)
                smooth_y = int(SMOOTHING * prev_car_pos[1] + (1 - SMOOTHING) * limited_y)

                car_pos = [smooth_x, smooth_y]
                prev_car_pos = car_pos.copy()

                # --- REBUILD RECT ---
                w = int(max(xs) - min(xs))
                h = int(max(ys) - min(ys))

                car_rect = pygame.Rect(
                    car_pos[0] - w//2,
                    car_pos[1] - h//2,
                    w,
                    h
                )

                # --- POLYGON (visual only, not smoothed) ---
                car_polygon = [(int(p[0]), int(p[1])) for p in mapped]

            else:
                car_rect = None
                car_polygon = None

    # --- DRAW GAME ---
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255,255,255), (0,0,WIDTH,HEIGHT), 3)

    # --- OBSTACLES ---
    for obs in obstacles:
        color = (255, 0, 0)

        if car_rect:
            expanded = obs.inflate(25, 25)

            if expanded.colliderect(car_rect):
                color = (255, 165, 0)

            if obs.colliderect(car_rect):
                color = (0, 0, 255)

        pygame.draw.rect(screen, color, obs)

    # --- DEBUG CORNERS ---
    if H_cam_to_game is not None:
        for mid in [1,2,3,4]:
            if mid in marker_dict:
                pt = np.array([[marker_dict[mid]]], dtype=np.float32)
                mapped = cv2.perspectiveTransform(pt, H_cam_to_game)
                x, y = mapped[0][0]
                pygame.draw.circle(screen, (0, 0, 255), (int(x), int(y)), 8)

    # --- DRAW CAR ---
    if car_polygon:
        pygame.draw.polygon(screen, (0,255,0), car_polygon, 2)

    if car_rect:
        pygame.draw.rect(screen, (0,255,0), car_rect, 2)
    else:
        pygame.draw.circle(screen, (0,255,0), car_pos, 10)

    pygame.display.flip()

    # --- PYGAME → OPENCV ---
    frame_game = pygame.surfarray.array3d(screen)
    frame_game = np.transpose(frame_game, (1, 0, 2))
    frame_game = cv2.cvtColor(frame_game, cv2.COLOR_RGB2BGR)

    # --- PROJECTOR ---
    H_proj = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(frame_game, H_proj, (WIDTH, HEIGHT))

    if mode == "calibrate":
        for i, pt in enumerate(dst_pts):
            pt_int = tuple(pt.astype(int))
            cv2.circle(warped, pt_int, RADIUS, (0,255,255), -1)
            cv2.putText(warped, str(i), pt_int,
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    cv2.imshow("Projection", warped)
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    clock.tick(60)

cap.release()
pygame.quit()
cv2.destroyAllWindows()