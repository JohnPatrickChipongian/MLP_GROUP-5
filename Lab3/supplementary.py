import cv2

import matplotlib.pyplot as plt


img = cv2.imread('Eren.jpg')
blur = cv2.blur(img,(10,10))
Gblur= cv2.GaussianBlur(img,(7,7),0)
Mblur = cv2.medianBlur(img,7)
BIblur = cv2.bilateralFilter(img,10,100,100)


cv2.putText(img,"ORIGINAL", (13,50), cv2.FONT_HERSHEY_SIMPLEX,1.5,255,5,0)
plt.imshow(img)
cv2.putText(blur,"AVERAGING", (13,50), cv2.FONT_HERSHEY_SIMPLEX,1.5,255,5,0)
plt.imshow(blur)
cv2.putText(Gblur,"GAUSSIAN BLUR", (13,50), cv2.FONT_HERSHEY_SIMPLEX,1.5,255,5,0)
plt.imshow(Gblur)
cv2.putText(Mblur,"MEDIAN BLUR", (13,50), cv2.FONT_HERSHEY_SIMPLEX,1.5,255,5,0)
plt.imshow(Mblur)
cv2.putText(BIblur,"BILATERAL FILTER", (13,50), cv2.FONT_HERSHEY_SIMPLEX,1.5,255,5,0)
plt.imshow(BIblur)


plt.subplot(3,3,1),plt.imshow(blur)
plt.xticks([]), plt.yticks([])

plt.subplot(3,3,3),plt.imshow(Gblur)
plt.xticks([]), plt.yticks([])

plt.subplot(3,3,5),plt.imshow(img)
plt.xticks([]), plt.yticks([])

plt.subplot(3,3,7),plt.imshow(Mblur)
plt.xticks([]), plt.yticks([])

plt.subplot(3,3,9),plt.imshow(BIblur)
plt.xticks([]), plt.yticks([])

plt.show()



plt.waitforbuttonpress()
plt.close('all')