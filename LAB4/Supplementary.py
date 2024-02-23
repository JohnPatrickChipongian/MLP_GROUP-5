import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'MJPG')
out = cv.VideoWriter('Group5_Output.avi', fourcc, 20.0, (640,  480))

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't recieve frame (stream end?). Exiting...")
        break

    sobelx = cv.Sobel(src=frame, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
    filtered_image_x = cv.convertScaleAbs(sobelx)

    edges = cv.Canny(frame, 100, 200)

    laplacian = cv.Laplacian(frame, 5, cv.CV_64F)
    filtered_image_x = cv.convertScaleAbs(laplacian)

    plt.figure(figsize=(20, 20))

    plt.subplot(221)
    plt.imshow(frame, cmap='gray')
    plt.title('Original')
    plt.axis("off")

    plt.subplot(222)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny edge detector')
    plt.axis("off")

    plt.subplot(223)
    plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel edge detector')
    plt.axis("off")

    plt.subplot(224)
    plt.imshow(laplacian, cmap='gray')
    plt.title('laplacian edge detector')
    plt.axis("off")

    plt.show()

    #cv.imshow('VideoCamera ', frame)
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()