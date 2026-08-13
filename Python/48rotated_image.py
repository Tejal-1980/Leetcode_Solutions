# 48. Rotate ImageYou are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

def rotate(self, matrix):
 n=len(matrix)
 for i in range(n):
  for j in range(i+1,n):
   #transpose
   matrix[i] , matrix[j]=matrix[j],matrix[i] 
   #reverse
 for i in range(n):
  matrix[i].reverse()

