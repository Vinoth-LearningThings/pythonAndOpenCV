from PIL import Image
import numpy as np
import cv2

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture('airport_footage.mp4')

def dhash(image, hash_size = 8):
        # Grayscale and shrink the image in one step.
        image = image.convert('L').resize(
            (hash_size + 1, hash_size),
            Image.ANTIALIAS,
        )

        pixels = list(image.getdata())

        # Compare adjacent pixels.
        difference = []
        for row in xrange(hash_size):
            for col in xrange(hash_size):
                pixel_left = image.getpixel((col, row))
                pixel_right = image.getpixel((col + 1, row))
                difference.append(pixel_left > pixel_right)

        # Convert the binary array to a hexadecimal string.
        decimal_value = 0
        hex_string = []
        for index, value in enumerate(difference):
            if value:
                decimal_value += 2**(index % 8)
            if (index % 8) == 7:
                hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
                decimal_value = 0

        return ''.join(hex_string)

def hamming2(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)

    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
                                     
while(cam.isOpened()):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = faceDetect.detectMultiScale(gray, 1.3, 5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0), 2)
        image = Image.fromarray(img[y:y+h,x:x+w])
        print dhash(image)
    cv2.namedWindow('faceDetector',cv2.WINDOW_NORMAL);
    cv2.resizeWindow('faceDetector', 600,300);
    cv2.imshow("faceDetector", img);
    
    if(cv2.waitKey(1) == ord('q')):
        break;

cam.release()
cv2.destroyAllWindows()
