import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
# img[:] = 255,0,0 #gives blue image

''' Draw a line through the image '''

cv2.line(img,(0,0),(500,500),(0,255,0),4)

'''Draw a rectangle'''
cv2.rectangle(img,(0,0),(200,300),(0,0,250),4)
# cv2.rectangle(img,(0,0),(200,300),(0,0,250),4, cv2.FILLED)

'''Draw a circle'''
cv2.circle(img,(100,100),50,(255,0,250),4)


'''Put in Text in the image'''
cv2.putText(img, "Yash is Great", (250,250), cv2.FONT_HERSHEY_PLAIN, 1,(0,255,130), 1)

cv2.imshow("Black Image", img)
cv2.waitKey(0)