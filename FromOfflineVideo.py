import numpy as np
import cv2

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture('airport_footage.mp4');

print cam.isOpened();

while(cam.isOpened()):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = faceDetect.detectMultiScale(gray, 1.3, 5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0), 2)
    cv2.namedWindow('faceDetector',cv2.WINDOW_NORMAL);
    cv2.resizeWindow('faceDetector', 600,300);
    cv2.imshow("faceDetector", img);
    
    if(cv2.waitKey(1) == ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
