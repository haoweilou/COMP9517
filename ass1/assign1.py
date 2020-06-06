import cv2
import numpy as np

new = np.zeros(shape=(100,100),dtype = np.uint8)
for i in range(100):
    for j in range(100):
        new[i][j] = 267+i
cv2.imwrite("test.png",new)
    
