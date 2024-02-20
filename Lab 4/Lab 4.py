import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread('mp.jpg')


sobelx = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
filtered_image_x = cv.convertScaleAbs(sobelx)

##sobely = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
##filtered_image_y = cv.convertScaleAbs(sobelx)

##sobelxy = cv.Sobel(src=img, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
##filtered_image_xy = cv.convertScaleAbs(sobelx)

laplacian = cv.Laplacian(img,5,cv.CV_64F)
filtered_image_x=cv.convertScaleAbs(laplacian)

canny = cv.Canny(img,100,200)


plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.imshow(sobelx, cmap='Blues')
plt.title('insert your title')
plt.axis("off")

plt.subplot(222)
plt.imshow(laplacian, cmap='gray')
plt.title('insert your title')
plt.axis("off")

plt.subplot(223)
plt.imshow(canny, cmap='gray')
plt.title('insert your title')
plt.axis("off")

plt.subplot(224)
plt.imshow(img, cmap='gray')
plt.title('insert your title')
plt.axis("off")

plt.show()
