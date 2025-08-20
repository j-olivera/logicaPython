import numpy as np

matrizMarco = np.empty([10,10],dtype=int)

for i in range(10):
    for j in range(10):
        if i==0 or i==10-1 or j==0 or j==10-1:
            matrizMarco[i][j]=1
        else:
            matrizMarco[i][j]=0

print(matrizMarco)

matrizDiagonal = np.empty([10,10],dtype=int)

for i in range(10):
    for j in range(10):
        if i==j:
            matrizDiagonal[i][j]=1
        else:
            matrizDiagonal[i][j]=0

print(matrizDiagonal)

matrizDiagonalS = np.empty([10,10],dtype=int)

for i in range(10):
    for j in range(10):
        if i+j==10-1:
            matrizDiagonalS[i][j]=1
        else:
            matrizDiagonalS[i][j]=0

print(matrizDiagonalS)