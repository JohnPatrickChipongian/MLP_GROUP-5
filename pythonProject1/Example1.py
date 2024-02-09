import cv2
img = cv2.imread("KingCobra.jpg", cv2.IMREAD_COLOR)

cv2.imshow("KingCobra.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()