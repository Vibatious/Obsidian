import cv2 as cv

raw  = cv.imread("../Res/input_image2.png",1)

print(raw[0][0])
raw[0][0][0] = 0
print(raw[0][0])