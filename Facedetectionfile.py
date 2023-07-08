# pip install opencv-python
# haarcascade_frontalface_default.xml

print("JKM, JPD, JVD, JHD")

import cv2

cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# data file


cap = cv2.VideoCapture(0)
# turn on the video (Web camera)
# utilized VideoCapture functions
# infinite loop
while True:                 
    ret, img = cap.read()
    print(ret)
    
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cvt convert color from bgr to grey scale

    f = cascade_face.detectMultiScale(g, 1.3, 4)

    # given data of frame. length, width and height
    for (x, y, w, h) in f:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 4)
        
        # x and w is in horizontal, y and h is in vertical.
        # (0,0,255) (B,G,R)
        # 4 is width of rectangle

    cv2.imshow('img', img)
    # to display
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destoryAllWindows()

