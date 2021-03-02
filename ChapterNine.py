#Detecting Shapes and Contours
import cv2
import numpy as np

print("Server Connected...")

def getContours(img):
    _,contours,_ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        #For a certain size of figures only
        if (area > 500):
            cv2.drawContours(imgContour, cnt, -1, (255,0,0),3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            '''Assigning objects according to the number of sides 
                and aspect ratio(division of width and height)'''

            if objCor == 3:
                objecType = "Tri"
            elif objCor == 4:
                aspectRation = w/float(h)
                if(aspectRation>0.95 and aspectRation<1.05):
                    objecType = "Square"
                else:
                    objecType = "Rectangle"
            elif objCor>4:
                objecType = "Circle"
            else:
                objecType = None

            cv2.rectangle(imgContour,(x,y),(x+w, y+h), (0,255,0), 2)
            cv2.putText(imgContour, objecType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_PLAIN, 0.7,
                        (0,0,0), 2)





img = cv2.imread("Resources/shapes.png")
imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)


getContours(imgCanny)

cv2.imshow("Original", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Blur", imgContour)
cv2.waitKey(0)