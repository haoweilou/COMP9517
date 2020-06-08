import numpy as np 
import cv2

A = np.zeros((100,100),dtype=np.int)
for i in range(100):
    for j in range(100):
        A[i][j] = -10
cv2.imwrite("Test.jpg",A)