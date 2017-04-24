import cv2
import numpy as np
import urllib

bgsMOG = cv2.BackgroundSubtractorMOG()
stream=urllib.urlopen("http://192.168.0.103:8080/video?x=y");
#cap    = cv2.VideoCapture("HD_Footage.mp4")
bytes=''
counter = 0

while True:
        #ret, frame = cap.read()
        bytes+=stream.read(16384)
        a = bytes.find('\xff\xd8')
        b = bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            jpg = bytes[a:b+2]
            bytes= bytes[b+2:]
            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)           
            fgmask = bgsMOG.apply(img, None, 0.01)
            cv2.line(img,(0,200),(350,200),(255,255,0),1)
            # To find the countours of the Cars
            contours, hierarchy = cv2.findContours(fgmask,
                                    cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            try:
                hierarchy = hierarchy[0]

            except:
                hierarchy = []

            for contour, hier in zip(contours, hierarchy):
                (x, y, w, h) = cv2.boundingRect(contour)

                if w > 20 and h > 20:
                    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 1)

                    #To find centroid of the Car
                    x1 = w/2      
                    y1 = h/2

                    cx = x+x1
                    cy = y+y1
##                    print "cy=", cy
##                    print "cx=", cx
                    centroid = (cx,cy)
##                    print "centoid=", centroid
                    # Draw the circle of Centroid
                    cv2.circle(img,(int(cx),int(cy)),2,(0,0,255),-1)

                    # To make sure the Car crosses the line
##                    dy = cy-108
##                    print "dy", dy
                    if centroid > (27, 38) and centroid < (134, 108):
##                        if (cx <= 132)and(cx >= 20):
                        counter +=1
##                            print "counter=", counter
##                    if cy > 10 and cy < 160:
                    cv2.putText(img, str(counter), (x,y-5),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.5, (255, 0, 255), 2)
##            cv2.namedWindow('Output',cv2.cv.CV_WINDOW_NORMAL)
            cv2.imshow('Output', img)
##          cv2.imshow('FGMASK', fgmask)


            key = cv2.waitKey(60)
            if key == 27:
                break

cap.release()
cv2.destroyAllWindows()
