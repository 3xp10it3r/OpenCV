import cv2
import numpy as np
img = cv2.imread('resources/a.jpg')

width,height = 250,350
# cv2.imshow("output",img)
pts1 = np.float32([[149,335],[406,341],[113,700],[490,695]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgWarp = cv2.warpPerspective(img,matrix,(width,height))
img = cv2.resize(img,(500,500))
cv2.imshow("output",img)
cv2.imshow("warpIMG",imgWarp)
cv2.waitKey(0)

