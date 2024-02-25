import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't recieve frame (stream end?). Exiting...")
        break

    sobelx = cv.Sobel(src=frame, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
    filtered_image_xy = cv.convertScaleAbs(sobelx)

    edges = cv.Canny(frame, 100, 200)

    laplacian = cv.Laplacian(frame, 5, cv.CV_64F)
    filtered_image_x = cv.convertScaleAbs(laplacian)

    cv.imshow('Original',frame)
    cv.imshow('Sobel', filtered_image_xy)
    cv.imshow('Canny', edges)
    cv.imshow('Laplacian', filtered_image_x)

    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()