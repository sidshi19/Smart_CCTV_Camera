import cv2

drawing = False
x1, y1, x2, y2 = -1, -1, -1, -1
selection_complete = False

def select(event, x, y, flags, param):
    global x1, y1, x2, y2, drawing, selection_complete

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x1, y1 = x, y
        x2, y2 = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            x2, y2 = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x2, y2 = x, y
        selection_complete = True
        print(f'Selected region: ({x1}, {y1}) to ({x2}, {y2})')

def rect_noise():
    global x1, y1, x2, y2, drawing, selection_complete

    cap = cv2.VideoCapture(0)
    cv2.namedWindow("select_region")
    cv2.setMouseCallback("select_region", select)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if drawing or selection_complete:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow("select_region", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        if selection_complete:
            cv2.destroyAllWindows()
            print("Selection complete.")
            break

    if not selection_complete:
        cap.release()
        cv2.destroyAllWindows()
        return

    while True:
        ret, frame1 = cap.read()
        ret, frame2 = cap.read()
        if not ret:
            break

        frame1only = frame1[y1:y2, x1:x2]
        frame2only = frame2[y1:y2, x1:x2]

        diff = cv2.absdiff(frame2only, frame1only)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        diff = cv2.blur(diff, (5, 5))
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            max_cnt = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame1, (x + x1, y + y1), (x + w + x1, y + h + y1), (0, 255, 0), 2)
            cv2.putText(frame1, "MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
        else:
            cv2.putText(frame1, "NO MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)

        cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 0, 255), 1)
        cv2.imshow("Motion Detection", frame1)

        if cv2.waitKey(1) & 0xFF == 27:
            drawing = False
            x1, y1, x2, y2 = -1, -1, -1, -1
            selection_complete = False
            break

    cap.release()
    cv2.destroyAllWindows()