#this file is gonna make that our image will cut in some part , in the video this chapter cut a image of cards and just
#it let a card

import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")

width,height = 250,350

cv2.imshow("Image",img)
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Output",imgOutput)
cv2.waitKey(0 )