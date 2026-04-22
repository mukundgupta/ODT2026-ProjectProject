import cv2
import numpy as np

cap = cv2.VideoCapture(0)

aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, rejected = detector.detectMarkers(gray)

    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        for i, corner in enumerate(corners):
            c = corner[0]

            # --- CENTER ---
            center_x = int(c[:, 0].mean())
            center_y = int(c[:, 1].mean())
            
            center = c.mean(axis=0).astype(int)
            # vector from corner 0 → corner 1
            dx = c[1][0] - c[0][0]
            dy = c[1][1] - c[0][1]

            angle = np.arctan2(dy, dx)

            

            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            # --- ID ---
            marker_id = ids[i][0]
            cv2.putText(frame, f"ID: {marker_id}", (center_x, center_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            
            for corner in corners:
                c = corner[0].astype(int)

                # Draw thicker polygon
                cv2.polylines(frame, [c], True, (0, 0, 255), 4)  # red, thickness=4

                # Draw corner points
                for point in c:
                    cv2.circle(frame, tuple(point), 6, (255, 0, 0), -1)
                
            end_point = (int(center[0] + dx), int(center[1] + dy))

            # draw center
            cv2.circle(frame, tuple(center), 6, (0, 255, 255), -1)

            # draw direction arrow
            cv2.arrowedLine(frame, tuple(center), end_point, (255, 0, 255), 3)

            print("ID:", marker_id, "Position:", center_x, center_y)
            print("Angle:", angle)
    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
