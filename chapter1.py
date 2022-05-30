import cv2
#Read images , videos , webcam

print("Package Imported")

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #ord q is to exit´s program 
        break


''' Opened the video source
cap = cv2.VideoCapture("Resources/test_video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
'''
''' Opened the Image source
img = cv2.imread('Resources/image.png')

cv2.imshow("Output",img)
#zero it means to infinite
# one thousand it means to one minute
cv2.waitKey(0)
'''