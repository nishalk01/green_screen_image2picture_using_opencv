import os
os.system("pip install opencv-python")#if u are running the code for the first time 
os.system("pip install numpy")#in case u dont have the modules,comment after running the code once 
import cv2
import numpy as np
img=cv2.imread('one_punch.jpg')
background1=cv2.imread('windows.jpg')
x=img.shape[0]
y=img.shape[1]
background=cv2.resize(background1,(x,y))
img=cv2.resize(img,(x,y))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_green=np.array([65,60,60])
upper_green=np.array([80,255,255])
mask=cv2.inRange(hsv,lower_green,upper_green)
lower_green=np.array([44,54,63])
upper_green=np.array([71,255,255])
mask_=cv2.inRange(hsv,lower_green,upper_green)
mask=mask_+mask
mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
mask=cv2.dilate(mask,np.ones((3,3),np.uint8),iterations=1)
mask0=cv2.bitwise_not(mask)
res1=cv2.bitwise_and(background,background, mask=mask)
res2=cv2.bitwise_and(img,img,mask=mask0)
out=cv2.addWeighted(res1,1,res2,1,0)
x_=background1.shape[0]
y_=background1.shape[1]
out=cv2.resize(out,(y_,x_))
cv2.imwrite('out1.jpg',out)
cv2.imshow('s',out)
cv2.waitKey(0)
cv2.destroyAllWindows()
