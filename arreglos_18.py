import numpy as np
import random
filas = int(input("Ingrese la cantidad de filas: "))
columnas= int(input("Ingrese la cantidad de columnas: "))

matriz= np.zeros([filas,columnas],dtype=int)
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=random.randint(0,9)

matrizTrans=np.zeros([columnas,filas],dtype=int)

for i in range(filas):
    for j in range(columnas):
        matrizTrans[j][i]=matriz[i][j]

print(matriz)
print(matrizTrans)