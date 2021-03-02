import cv2
import numpy as np

print("File Running...")
img = cv2.imread("Resources/lena.png")

''' Function 1. cvtColor --> Converts Colored image to GrayScale'''
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Output", imgGray)

''' Function 2. GaussianBlur --> Converts image to Blurred Image'''
imgBlur = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow("Blur Image", imgBlur)

''' Function 3. Canny --> Edge Detection of the Image'''
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("Blur Image", imgCanny)

''' Function 4. dialation --> Edge Detection of the Image with thicker lines(more defined)'''
kernel = np.ones((5,5), np.uint8)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("Dialated Imagae", imgDialation)

''' Function 4. errode --> Edge Detection of the Image with thinner edges'''
imgErosion = cv2.erode(imgCanny, kernel, iterations=1)
cv2.imshow("Eroded Image", imgErosion)
cv2.waitKey(0)

