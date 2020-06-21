import cv2
import numpy as np

path = "COMP9517_20T2_Lab2_Image.jpg"
img = cv2.imread(path);
sift= cv2.xfeatures2d_SIFT();
keypoints, _ = sift.detectAndCompute(img,None)
print(1)

out = img
img = cv2.drawKeypoints(image=img,keypoints=keypoints,outImage=out)

cv2.imwrite("temp.png",out)