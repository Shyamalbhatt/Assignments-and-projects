import numpy as np
M1 = [[8, 14, -6], 
      [12,7,4], 
      [-11,3,21]]

M2 = [[3, 16, -6],
           [9,7,-4], 
           [-1,3,13]]

M3  = [[0,0,0],
       [0,0,0],
       [0,0,0]]
matrix_length = len(M1)
for i in range(len(M1)):
    for k in range(len(M2)):
            M3[i][k] = M1[i][k] + M2[i][k]

print("The sum of Matrix M1 and M2 = ", M3)
for i in range(len(M1)):
    for k in range(len(M2)):
            M3[i][k] = M1[i][k] * M2[i][k]

print("The multiplication of Matrix M1 and M2 = ", M3)
M1 = np.array([[3, 6, 9], [5, -10, 15], [4,8,12]])
M2 = M1.transpose()

print(M2)
