import cv2
import numpy as np

Cells = 'Cells.png'
Particles = 'Particles.png'

Cells_img = cv2.imread(Cells,-1)
Particles_img = cv2.imread(Particles,-1)


print('Pless enter the value of N: ')
N = int(input())
I = Particles_img.shape

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
    cv2.imwrite('A.jpg',A)

