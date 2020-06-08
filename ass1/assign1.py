# Written by Haowei Lou
# z5258575
# 05 June 2020
import cv2
import numpy as np

Cells = 'Cells.png'
Particles = 'Particles.png'

# Load image path and find the height and width of the image
Image_path = Cells
Image = cv2.imread(Image_path,0)
I = Image.shape
height = I[0]
width = I[1]

# Enter the value of n
print('Pless enter the value of N: ',end='')
N = int(input())

# Function that find the maximum value in neighbours
def maxfilter(image,row,col):
    start = [row-N//2,col-N//2]
    start[0] = max(0,start[0])
    start[1] = max(0,start[1])
    if start[0] > height - N:
        start[0] = height - N
    if start[1]  > width - N:
        start[1] = width - N

    return np.max(image[start[0]:start[0]+N,start[1]:start[1]+N])

# Function that find the minimum value in neighbours
def minfilter(image,row,col):
    start = [row-N//2,col-N//2]
    start[0] = max(0,start[0])
    start[1] = max(0,start[1])
    if start[0] > height - N:
        start[0] = height - N
    if start[1]  > width - N:
        start[1] = width - N

    return np.min(image[start[0]:start[0]+N,start[1]:start[1]+N])

#Ask user to enter M value
print('Pless enter the value of M: ',end='')
M = int(input())

#Initialise image
A = np.zeros(I,dtype=np.int16)
B = np.zeros(I,dtype=np.int16)
O = np.zeros(I,dtype=np.int16)
if M == 0:
    for i in range(height):
        for j in range(width):
            A[i][j] = maxfilter(Image,i,j)
    for i in range(height):
        for j in range(width):
            B[i][j] = minfilter(A,i,j)
    matrix_255 = np.empty(I)
    matrix_255.fill(255)
    O = Image - B + matrix_255
elif M == 1:
    for i in range(height):
        for j in range(width):
            A[i][j] = minfilter(Image,i,j)
    for i in range(height):
        for j in range(width):
            B[i][j] = maxfilter(A,i,j)
    O = Image - B

#Output image
cv2.imwrite("A.png",A)
cv2.imwrite("B.png",B)
cv2.imwrite("O.png",O)