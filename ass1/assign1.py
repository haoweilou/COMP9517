import cv2
import numpy as np

print('Enter the path of image: ')
Image_path = str(input())
Image = cv2.imread(Image_path,-1)
I = Image.shape
height = I[0]
width = I[1]
print('Pless enter the value of N: ')
N = int(input())
I = Image.shape

height = I[0]
width = I[1]
def find_area(input,n):
    row = input[0]
    col = input[1]
    top_left = (max(0,row-n),max(0,col-n))
    down_right = (min(height,row+n),min(width,col+n))
    return top_left,down_right

def find_max_in_neighbour():
    output = 0
    return output
if __name__ == '__main__':
    A = np.zeros(I,dtype=np.uint8)
    N = N-1
    for i in range(height):
        for j in range(width):
            A[i][j] = i+j
    c

