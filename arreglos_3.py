import random
import numpy as np

def ordenamientoBurbuja(arreglo):
    for i in range(len(arreglo)-1):
        for j in range(len(arreglo)-1-i):
            if(arreglo[j]>arreglo[j+1]):
                tmp=arreglo[j+1]
                arreglo[j+1]=arreglo[j]
                arreglo[j]=tmp

def buscarNis(arreglo):
    nis = int(input("Ingrese el NIS a buscar: "))
    for i in range(len(arreglo)):
        if nis==arreglo[i]:
            print("NIS ENCONTRADOR EN LA POSICION ",i+1)
            return
    print("No se ha encontrado el NIS")

def main():
    
    pendienteLuz = np.zeros([20],dtype=int)
    for i in range(20):
        pendienteLuz[i] = random.randint(0,50000)
    
    print("Pendientes sin ordenar: ", pendienteLuz)
    ordenamientoBurbuja(pendienteLuz)
    print("Pendientes ordenados: ",pendienteLuz)
    buscarNis(pendienteLuz)

main()


