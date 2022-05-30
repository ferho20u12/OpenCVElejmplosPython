import  cv2
import  numpy as np
#import imutils
import  os

Datos = 'n'

if not os.path.exists(Datos):
    print("carpeta creada",Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture(2,cv2.CAP_DSHOW)

x1,y1=190,80
x2,y2=450,398

count = 0
'''
    while True:
    ret,frame = cap.read()
    if ret == False : break
    inAux = frame.copy()
    withImage=50
    heightImage=90
    #crop_img = img[y:y + h, x:x + w]
    imagenRecortada  = inAux[200:200+withImage,0:heightImage]
    #: imagen[fila inicial : fila final, columna inicial : columna final]
    imagenRecortada2 = frame.copy()[90:withImage,200:200+heightImage]
    imagenRecortada3 = frame.copy()[180:withImage,200:200+heightImage]
    imagenRecortada4 = frame.copy()[270:withImage,200:200+heightImage]
    imagenRecortada5 = frame.copy()[360:withImage,200:200+heightImage]
    withImage=70
    heightImage=90
    cv2.rectangle(frame,(0,200+heightImage),(withImage,heightImage+90),(0,255,0),1)
    cv2.rectangle(frame, (withImage,200+heightImage), (withImage, heightImage+90), (0, 255, 0), 1)
    cv2.rectangle(frame, (withImage*2,200+heightImage), (withImage, heightImage+90), (0, 255, 0), 1)
    cv2.rectangle(frame, (withImage*3,200+heightImage), (withImage, heightImage+90), (0, 255, 0), 1)
    cv2.rectangle(frame, (withImage*4,200+heightImage), (withImage, heightImage+90), (0, 255, 0), 1)
    #objeto = imutils.resize(objeto,width= 224)

    cv2.imshow('Imagen Original', frame)
    cv2.imshow('Imagen Recortada', imagenRecortada)
    cv2.imshow('Imagen Recortada2', imagenRecortada2)
    cv2.imshow('Imagen Recortada3', imagenRecortada3)
    cv2.imshow('Imagen Recortada4', imagenRecortada4)
    cv2.imshow('Imagen Recortada5', imagenRecortada5)
    k = cv2.waitKey(1)
    if k == 27:
        
    if k == ord('s'):
        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),frame)
        print("Imagen almacenada: ",'objeto_{}.jpg'.format(count))
        count = count+1

'''
cap.release()
cv2.destroyAllWindows()
