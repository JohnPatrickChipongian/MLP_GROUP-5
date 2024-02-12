import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Midoriya.jpg')
median = cv.medianBlur(img,5)


plt.subplot(121),plt.imshow(img),plt.title('original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()