import cv2
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
videoCapture = cv2.VideoCapture(0)

while True:
    #Yuz Tanimlama Kismi
    ret, frame =videoCapture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    #Etraftaki Diktortgeni Olusturualim

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)#sondaki deger kalinligi onun bir solundaki ise rengi belirler.
    cv2.imshow('Video', frame)

    #uygulamadan cikmak icin q tusunu kullanalim
    if(cv2.waitKey(1) & 0XFF == ord('q')):
        break

videoCapture.release()
cv2.destroyAllWindow()
