#shapes and text
import cv2
import  numpy as np

img = np.zeros((512,512,3),np.uint8)

#print(img.shape)
#img[200:300,100:300]=255,0,0 #draw lines
#line
cv2.line(img,(0,0), (img.shape[0],img.shape[0]),(0,255,0),2)
          # position       x           y     color  size

#rectangule
cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)#cv2.FILLED

#circle
cv2.circle(img,(400,50),30,(255,255,0),cv2.FILLED)

#put text
cv2.putText(img," OpenCv ",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1 )


cv2.imshow("Image",img)
cv2.waitKey(0)