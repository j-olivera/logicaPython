import numpy as np

def darValores(vector,n):
    for i in range(0,n) :
        vector[i]=int(input(f"Valor para la posicion {i+1}: "))

def mostrarValores(vector):
    for elemento in vector:
        print(elemento,end=" ")

def minimo(vector):
    minimo=999
    for elemento in vector:
        if elemento<minimo:
            minimo=elemento
    print(f"\nMenor elemento del vector C: {minimo}")

def maximo(vector):
    maximo=-1
    for elemento in vector:
        if elemento>maximo:
            maximo=elemento
    print(f"\nMayor elemento del vector C: {maximo}")

while True:
    n = int(input("Ingresa un tamaño para los vectores: "))
    if(n<=1):
        print("Ingrese un tamaño mayor a 1.")
    else:
        break
#
arregloA = np.zeros([n],dtype=int)
arregloB = np.zeros([n],dtype=int)
#
print("Valores para el arreglo A.\n")
darValores(arregloA,n)
print("Valores para el arreglo B.\n")
darValores(arregloB,n)
#
arregloC = arregloA+arregloB
#
print("Vector C: ",end=" ")
mostrarValores(arregloC)
minimo(arregloC)
maximo(arregloC)
