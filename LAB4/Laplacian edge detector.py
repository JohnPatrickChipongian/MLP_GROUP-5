import cv2 as cv
from matplotlib import pyplot as plt


orig =cv.imread('mp.jpg')
img = cv.cvtColor(orig, cv.COLOR_BGR2RGB)

laplacian = cv.Laplacian(img,5,cv.CV_64F)
filtered_image_x = cv.convertScaleAbs(laplacian)

plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis("off")

plt.subplot(222)
plt.imshow(laplacian, cmap='gray')
plt.title('Canny edge detector')
plt.axis("off")

plt.show()