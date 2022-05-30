import cv2
import  numpy as np
#this part we gonna joining image


img = cv2.imread('Resources/image.png')


'''
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Image",imgHor)
cv2.imshow("Image Vertical",imgVer)
'''
cv2.waitKey(0)