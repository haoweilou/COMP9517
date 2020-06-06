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
def find_region(input,n):
    row = input[0]
    col = input[1]
    start = [row-n//2,col-n//2]
    if start[0] < 0:
        start[0] = 0
    if start[1] < 0:
        start[1] = 0
    if start[0] + n > height:
        start[0] = height - n
    if start[1] + n > width :
        start[1] = width - n
    return start
def find_max(image,start):
    i = 0
    output = 0
    row = start[0]
    col = start[1]
    while i < N:
        j = 0
        while j < N:
            output = max(image[row+i][col+j],output)
            j += 1
        i += 1
    print(output)
    return output


def find_max_in_neighbour():
    output = 0
    return output
if __name__ == '__main__':
    A = np.zeros(I,dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            if(find_region((i,j),N) != [i,j]):
                start = find_region((i,j),N)
                A[i][j] = find_max(Image,start)
    cv2.imwrite("A.jpg",A)
    print(height,width)
    
