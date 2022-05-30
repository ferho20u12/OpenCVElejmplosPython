import cv2


cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_eye_tree_eyeglasses.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #ord q is to exit´s program
        break
