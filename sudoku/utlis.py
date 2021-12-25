import cv2
import numpy as np

pathImage = "1.jpg"
heightImg = 450
widthImg = 450

img = cv2.imread(pathImage)
img = cv2.resize(img, (widthImg, heightImg))
imgBlank = np.zeros((heightImg,widthImg,3),np.uint8)
imgTreshold = preProcess(img)

cv2.imshow("ImageWindow", img)
cv2.waitKey(0)