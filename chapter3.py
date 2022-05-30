
#cropped image and resize image

import  cv2
import numpy as np

img = cv2.imread("Resources/lamborgini.png")

print(img.shape)
                            #this is the size that we´ll put in the image
#we´ve created the new image
imgResize = cv2.resize(img,(300,200))
print(imgResize.shape) #print the image´s size

#cut some image
imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)