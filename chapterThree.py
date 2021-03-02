import cv2
import numpy as np

print("Server Connected...")

#Checking Image Shape
img = cv2.imread("Resources/lambo.PNG")
cv2.imshow("Image", img)
print(img.shape)

#Resizing Image
imgNew = cv2.resize(img,(200, 200))
cv2.imshow("New Image", imgNew)
print(imgNew.shape)

#Cropping Image
imgCropped = img[0:200, 200:500]
cv2.imshow("New Image", imgCropped)
cv2.waitKey(0)