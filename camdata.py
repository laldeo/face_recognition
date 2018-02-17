import cv2
camera = cv2.VideoCapture(0)
snum = 0
while True:
    return_value,image = camera.read()
    image = cv2.flip(image,1,0)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('laldeo',gray)
    if cv2.waitKey(1)& 0xFF == ord('n'):
    	snum += 1
        cv2.imwrite("snap/laldeo."+str(snum)+".jpg",gray)
    if(snum>2):
    	break
camera.release()
cv2.destroyAllWindows()
