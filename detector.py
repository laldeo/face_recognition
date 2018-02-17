import cv2,os
import numpy as np
from PIL import Image 
import pickle

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 2, 1) #Creates a font
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        #cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        if(Id==2):
            Id="unknown"
        elif(Id==1 ):
            Id="laldeo"     
        # elif(nbr_predicted==3):
        #     nbr_predicted='unknown'
        elif(Id==-2):
            Id="unknown"
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),3)
        cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255) #Draw the text
    cv2.imshow('lal-frame',im)
        #cv2.waitKey(10)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()









