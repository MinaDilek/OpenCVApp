import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # green
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # blue
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # pink
    lower_pink = np.array([160, 0, 0])
    upper_pink = np.array([180, 255, 255])
    pink_mask = cv2.inRange(hsv_frame, lower_pink, upper_pink)
    pink = cv2.bitwise_and(frame, frame, mask=pink_mask)

    # yellow
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, yellow_lower, yellow_upper)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

    cv2.imshow("Webcam", frame)
    cv2.imshow("Green Mask", green_mask)
    # cv2.imshow("Blue", blue)
    # cv2.imshow("Pink", pink)
    # cv2.imshow("Yellow", yellow)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
