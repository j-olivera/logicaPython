import numpy as np

def cargarArray(arreglo):
    k = int(input("Defina un numero k: "))
    for i in range(5):
        arreglo[i]=k*(i+1)

def main():
    n = int(input("Ingrese un numero: "))
    arreglo= np.zeros([n],dtype=int)
    cargarArray(arreglo)
    print(arreglo)

main()