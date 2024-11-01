import cv2
from datetime import datetime
import os

def in_out():
    cap = cv2.VideoCapture(0)

    # Initialize state variables
    right = False
    left = False

    # Ensure the directories exist
    if not os.path.exists('visitors/in'):
        os.makedirs('visitors/in')
    if not os.path.exists('visitors/out'):
        os.makedirs('visitors/out')

    while True:
        ret, frame1 = cap.read()
        if not ret:
            break
        frame1 = cv2.flip(frame1, 1)
        
        ret, frame2 = cap.read()
        if not ret:
            break
        frame2 = cv2.flip(frame2, 1)

        diff = cv2.absdiff(frame2, frame1)
        diff = cv2.blur(diff, (5, 5))
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        _, threshd = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
        contr, _ = cv2.findContours(threshd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        x_center = frame1.shape[1] // 2  # Center of the frame
        detected = False
        
        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_cnt)
            x_center_of_contour = x + w // 2

            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame1, "MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

            # Determine direction based on contour center position
            if x_center_of_contour > x_center + 100:
                right = True
                left = False
            elif x_center_of_contour < x_center - 100:
                left = True
                right = False
            detected = True
        
        if detected:
            if right:
                print("to right")
                cv2.imwrite(f"C:/Users/sgshi/OneDrive/Desktop/Projects/Smart CCTV/Visitors/out/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg", frame1)
                right = False  # Reset direction after saving

            elif left:
                print("to left")
                cv2.imwrite(f"C:/Users/sgshi/OneDrive/Desktop/Projects/Smart CCTV/Visitors/in/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg", frame1)
                left = False  # Reset direction after saving

        cv2.imshow("Frame", frame1)

        k = cv2.waitKey(1)
        if k == 27:  # Esc key to stop
            cap.release()
            cv2.destroyAllWindows()
            break


