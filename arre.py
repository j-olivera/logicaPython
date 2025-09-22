import numpy as np
import random

def cargarArreglo(arreglo,l):
    for i in range(l):
        arreglo[i]=random.randint(0,100)
    return
def mostarArreglo(arreglo,l):
    for i in range(l):
        print(arreglo[i]," ",end="")
    return
def ordenarArreglo(arreglo,l):
    for i in range(l):
        for j in range(l-i-1):
            if arreglo[j]>arreglo[j+1]:
                aux = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = aux
    return

def busquedaBinaria(arreglo,l,valor):
    izq=0
    der=l-1
    encontrado=False
    while izq<=der and encontrado==False:
        medio=(izq+der)//2
        if arreglo[medio]==valor:
            encontrado=True
        elif arreglo[medio]<valor:
            izq=medio+1
        else:
            der=medio-1
    if encontrado:
        print("valor encontrado en la posicion ", medio+1)
    else:
        print("\nValor no encontrado")

def main():
    l = int(input("Ingrese la longitud del arreglo: "))
    arreglo = np.zeros([l],dtype=int)
    cargarArreglo(arreglo,l)
    mostarArreglo(arreglo,l)
    ordenarArreglo(arreglo,l)
    print("")
    mostarArreglo(arreglo,l)
    busquedaBinaria(arreglo,l,22)
if __name__ == '__main__':
    main()