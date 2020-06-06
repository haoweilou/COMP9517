import cv2
import numpy as np

print('Enter the path of image: ')
Image_path = 'Particles.png'
Image = cv2.imread(Image_path,-1)
I = Image.shape
height = I[0]
width = I[1]
print('Pless enter the value of N: ')
N = int(input())
I = Image.shape

height = I[0]
width = I[1]
def find_max(input):
    row = input[0]
    col = input[1]
    start = [row-N//2,col-N//2]
    if start[0] < 0:
        start[0] = 0
    if start[1] < 0:
        start[1] = 0
    if start[0] + N > height:
        start[0] = height - N
    if start[1] + N > width :
        start[1] = width - N
    i = 0
    output = 0
    row = start[0]
    col = start[1]
    while i < N:
        j = 0
        while j < N:
            output = max(Image[row+i][col+j],output)
            j += 1
        i += 1
    return output
    
if __name__ == '__main__':
    A = np.zeros(I,dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            A[i][j] = find_max((i,j))
    cv2.imwrite("A.jpg",A)
    
