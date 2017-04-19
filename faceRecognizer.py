import cv2
import cv2.cv as cv

detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam= cv2.VideoCapture("HD_Footage.mp4")
cap = cv.CaptureFromFile("HD_Footage.mp4")

nframes=int(cv.GetCaptureProperty(cap,cv.CV_CAP_PROP_FRAME_COUNT))
fps= int(cv.GetCaptureProperty(cap,cv.CV_CAP_PROP_FPS))

print nframes

Id=raw_input('enter your id')
sampleNum=0

for f in xrange(nframes):
    ret, frameimg = cam.read()
    gray = cv2.cvtColor(frameimg, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frameimg,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('frame',frameimg)
        
    cv.WaitKey(1)

cam.release()
cv.DestroyAllWindows()
