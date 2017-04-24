import cv2
import urllib 
import numpy as np

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
stream=urllib.urlopen("http://192.168.0.103:8080/video?x=y");
bytes=''

while True:
    bytes+=stream.read(16384)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0), 2)
        cv2.namedWindow('faceDetector',cv2.WINDOW_NORMAL);
        cv2.resizeWindow('faceDetector', 600,300);
        cv2.line(img,(0,600),(950,600),(255,0,0),5)
        cv2.imshow("faceDetector", img);

        if(cv2.waitKey(1) == ord('q')):
            break;
    
cv2.destroyAllWindows()
