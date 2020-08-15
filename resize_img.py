import cv2

img = cv2.imread('resources/first.jpg')
print(img.shape)


#resizing Img
resized_img = cv2.resize(img,(1000,500))  #width , height
print(resized_img.shape)

# cropping Image
croppedImg = resized_img[0:500,400:800]


cv2.imshow("CropedImg",croppedImg)
cv2.imshow('img',img)
cv2.imshow("resized Img", resized_img)
cv2.waitKey(0)