import cv2 as cv
from matplotlib import pyplot as plt


img=cv.imread('mp.jpg')


sobelx = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
filtered_image_x = cv.convertScaleAbs(sobelx)

sobely = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
filtered_image_y = cv.convertScaleAbs(sobelx)

sobelxy = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
filtered_image_xy = cv.convertScaleAbs(sobelx)


plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis("off")

plt.subplot(222)
plt.imshow(sobelx, cmap='gray')
plt.title('sobelx')
plt.axis("off")

plt.subplot(223)
plt.imshow(sobely, cmap='gray')
plt.title('sobely')
plt.axis("off")

plt.subplot(224)
plt.imshow(sobelxy, cmap='gray')
plt.title('sobelxy')
plt.axis("off")


plt.show()