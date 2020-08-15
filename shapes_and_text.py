import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)
print(img)
# img[200:300,400:500] = 0,0,255   #BGR -- >> BLUE , GREEN , RED  

# cv2.line(img, (0,0) ,(512,512), (255,0,0) ,3)
cv2.line(img, (0,0) ,(img.shape[1],img.shape[0]), (255,0,0) ,3)
# cv2.rectangle(img,(0,0),(400,400),(0,0,255),cv2.FILLED)
cv2.rectangle(img,(0,0),(400,400),(0,0,255),2)

cv2.circle(img,(256,256),100,(0,255,0),2)

cv2.putText(img,"OpenCV",(205,255),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow("created Img",img)
cv2.waitKey(0)