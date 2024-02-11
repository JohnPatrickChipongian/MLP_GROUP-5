import numpy as np
import cv2 as cv
cap = cv.VideoCapture('JK_ED.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('VideoPlay', frame)
    if cv.waitKey(20) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()