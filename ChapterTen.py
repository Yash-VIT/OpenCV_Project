#Face Detection using openCV custom XML trained model
import cv2
print("Server Connected")
#Custom xml
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv2.imread("Resources/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting faces
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

#Loop for Rectangle
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow("Result", img)
cv2.waitKey(0)