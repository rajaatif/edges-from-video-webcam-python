import numpy as np
import cv2
def nothing(x):
    pass

threshold1=1000
threshold2=6000
#I specified the  name of window UI
cv2.namedWindow("canny")
#I specified the  name of Trackerbar UI
cv2.createTrackbar('threshold1','canny',2000,5000,nothing)
cv2.createTrackbar('threshold2','canny',2000,5000,nothing)
#I capturing the video from default camera
vc=cv2.VideoCapture(0)
ret,frame=vc.read()

while ret:
    ret,frame=vc.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos('threshold1', 'canny')
    threshold2 = cv2.getTrackbarPos('threshold2', 'canny')
    edge = cv2.Canny(gray, threshold1, threshold2, apertureSize=5)
    img = frame.copy()
    img = np.uint8(img/2.)
    img[edge != 0] = (0, 255, 0)
    r,c,cc=img.shape
    img1=cv2.getRotationMatrix2D((c/2,r/2),-0,1)
    img2=cv2.warpAffine(img,img1,(r,c))
    cv2.imshow('canny', img2)
    ch = cv2.waitKey(5)
    if ch == 27:
        break


# Destroy all windows
cv2.destroyAllWindows()
