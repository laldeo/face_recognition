import cv2
import numpy as np
import sqlite3
#from camtrainer import trainer

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

cam=cv2.VideoCapture(0);

def insertOrUpdate(Id,Name):
    conn=sqlite3.connect("Facedemo.db")
    cmd="SELECT * FROM Facepeople WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE Facepeople SET Name="+str(Name)+"WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO Facepeople(ID,Name) Values("+str(Id)+","+str(Name)+")"

    conn.execute(cmd)
    conn.close()

Id=raw_input('Enter User Id=')
name=raw_input('Enter User Name=')
insertOrUpdate(Id,name)
sampleNum=0
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);    
        cv2.imshow("Face",img);
        #cv2.waitKey(1);
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            cam.release()
            cv2.destroyAllWindows()

        elif k == ord('n'):
            cv2.waitKey(1);
            cv2.imwrite("dataSet/User."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            #trainer()
    if(sampleNum>20):
        break
cam.release()
cv2.destroyAllWindows()