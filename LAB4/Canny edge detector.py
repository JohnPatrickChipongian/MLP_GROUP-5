import cv2 as cv
from matplotlib import pyplot as plt


img=cv.imread('mp.jpg')

edges = cv.Canny(img,100,200)

plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis("off")

plt.subplot(222)
plt.imshow(edges, cmap='gray')
plt.title('Canny edge detector')
plt.axis("off")

plt.show()