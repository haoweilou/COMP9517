# Written by Haowei Lou
# z5258575
# 05 June 2020
import cv2
import numpy as np

Cells = 'Cells.png'
Particles = 'Particles.png'

# Load image path and find the height and width of the image
Image_path = Particles
Image = cv2.imread(Image_path,0)
I = Image.shape
height = I[0]
width = I[1]

# Enter the value of n
print('Pless enter the value of N: ',end='')
N = int(input())

# Function that find the maximum value in neighbours
def maxfilter(row,col):
    start = [row-N//2,col-N//2]

    start[0] = max(0,start[0])
    start[1] = max(0,start[1])
    if start[0] > height - N:
        start[0] = height - N
    if start[1]  > width - N:
        start[1] = width - N
    
    output = 0
    for i in range(0,N):
        for j in range(0,N):
            output = max(Image[start[0]+i][start[1]+j],output)
    return output

# Function that find the minimum value in neighbours
def minfilter(A,row,col):
    start = [row-N//2,col-N//2]

    start[0] = max(0,start[0])
    start[1] = max(0,start[1])
    if start[0] > height - N:
        start[0] = height - N
    if start[1]  > width - N:
        start[1] = width - N
    
    output = 255
    for i in range(0,N):
        for j in range(0,N):
            output = min(A[start[0]+i][start[1]+j],output)
    return output

A = np.zeros(I,dtype=np.int)
for i in range(height):
    for j in range(width):
        A[i][j] = maxfilter(i,j)

B = np.zeros(I,dtype=np.int)
for i in range(height):
    for j in range(width):
        B[i][j] = minfilter(A,i,j)

O = np.zeros(I,dtype=np.int)
for i in range(height):
    for j in range(width):
        O[i][j] = Image[i][j] - B[i][j] + 255


cv2.imwrite("A.png",A)
cv2.imwrite("B.png",B)
cv2.imwrite("O.png",O)
