import numpy as np
import random

def coordenadas(matriz):
    for i in range(15):
        for j in range(15):
            matriz[i][j]=i+j
    print(matriz) 

def randomp(matriz):
    for i in range(15):
        for j in range(15):
            if i==j:
                matriz[i][j] = random.randint(0,9)
    print(matriz)

def randoms(matriz):
    for i in range(15):
        for j in range(15):
            if i+j==14:
                matriz[i][j] = random.randint(0,9)
    print(matriz)

def main():
    matrizCoordenadas = np.zeros([15,15],dtype=int)
    matrizRandom = np.zeros([15,15],dtype=int)
    matrizsRandom = np.zeros([15,15],dtype=int)
    coordenadas(matrizCoordenadas)
    randomp(matrizRandom)
    randoms(matrizsRandom)

main()