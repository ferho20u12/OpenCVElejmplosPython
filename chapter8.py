import cv2
import  numpy as np
import  library as l
path = 'Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)
l.getContours(imgCanny,imgContour)

imgStack  = l.stackImages(0.6,([img,imgGray,imgBlur],
                               [imgCanny,imgBlank,imgContour]))


cv2.imshow("Stack",imgStack)
cv2.imshow("Image",imgContour)
cv2.waitKey(0)