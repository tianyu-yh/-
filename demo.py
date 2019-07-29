import cv2 as cv
import numpy as np
img = imread('2.jpg',1)
imgsize = img.shape
height = imgsize[0]
width = imgsize[1]
dst = np.zeros((height,width,3),np.uint8)
for i in range(100,200,10):   #10*10大小的马赛克区域，统一为第一个元素的灰度值
   for j in range(200,250,10):
    for m in range(0,10):
      for n in range(0,10):
        img[i+m,j+n] = img[m,n]
cv.imshow('aa',img)
cv.waitkey(0)
