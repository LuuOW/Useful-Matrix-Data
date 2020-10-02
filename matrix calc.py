import math
import numbers
import numpy as np

#Defines rows and columns count
R = int(input("Ingrese el numero de filas: ")) 
C = int(input("Ingrese el numero de columnas: ")) 
  
  
matrix = []
#Enter 1 by 1 the elements of the first row followed by the elements of the next rows, etc
print("Ingrese los elementos fila por fila:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a)

# for RREF
def rref(M):
        lead = 0
        rowCount = len(M)
        columnCount = len(M[0])
        for r in range(rowCount):
                if lead >= columnCount:
                        return
                i = r
                while (M[i][lead] == 0):
                        i += 1
                        if (i == rowCount):
                                i = r
                                lead += 1
                                if (columnCount == lead):
                                        return
                M[[r,i]] = M[[i,r]]

                if (M[r][lead] != 0):
                        M[r] = M[r]/M[r][lead]
                for i in range (rowCount):
                        if (i != r):
                                M[i] = M[i] - M[i][lead]*M[r]
                lead += 1

squareMatrix = False
if R == C:
    squareMatrix = True

#Find the determinant just if the input is a square Matrix
if squareMatrix == True:
    matrixDet = np.linalg.det(matrix)

#Find the inverse of the matrix just if the input is a square Matrix
if squareMatrix == True:
    matrixInverse = np.linalg.inv(matrix)

#Find the rank of the matrix
matrixRank = np.linalg.matrix_rank(matrix)

#Find the RREF of the matrix
matrixRREF = np.array(matrix)
matrixRREF = matrixRREF.astype(np.float)
rref(matrixRREF)

#Outputs

#print the original matrix
print("La matriz orginal es: \n", 
matrix)

#print the rank of the matrix
print("El rango de la matriz es: \n",
matrixRank)

#print the determinant of the matrix
print("El determinante de la matriz es: \n",
matrixDet)

#in case the determinant is not 0, print the inverse
if matrixDet != 0:
    print("La inversa de la matriz es: \n",
    matrixInverse)

#print the RREF
print("La RREF es: \n",
matrixRREF)