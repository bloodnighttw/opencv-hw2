import cv2

img = cv2.imread("test_noise.png")
light = cv2.imread(r"light.jpg")

cv2.imshow("original img",img)

cv2.namedWindow("medianBlur")
cv2.namedWindow("sub")
cv2.namedWindow("thresholding")

temp = cv2.medianBlur(img,3)
temp1 = light - temp
_,temp2 = cv2.threshold(temp1,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("medianBlur",temp)
cv2.imshow("sub",temp1)
cv2.imshow("thresholding",temp2)

cv2.waitKey(0)