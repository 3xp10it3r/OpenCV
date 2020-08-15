import cv2
import numpy as np

img = cv2.imread('resources/first.jpg')

kernel = np.ones((5,5),np.uint8)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(gray_img,(7,7),0)
cannyImg = cv2.Canny(gray_img,100,100)
imgdilation = cv2.dilate(cannyImg,kernel,iterations=1)
ErodedImg = cv2.erode(imgdilation,kernel,iterations=1)
cv2.imshow("GrayImage",gray_img)
cv2.imshow("BlurImage",imgBlur)
cv2.imshow("ErodedImage",ErodedImg)
cv2.imshow("CannyImage",cannyImg)
cv2.imshow("DilatedImage",imgdilation)
cv2.waitKey(0)