import numpy as np
import random
#
def cargarMatriz(matriz,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = random.randint(0,100)

def mostrarMatriz(matriz,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j],end=" ")
        print("")
def matriz_a_Arreglo(matriz,filas,columnas,arreglo):
    indice=0
    for i in range(filas):
        for j in range(columnas):
            arreglo[indice] = matriz[i][j]
            indice+=1
def mostrarArreglo(arreglo,longitud):
    for i in range(longitud):
        print(f"{arreglo[i]} ",end=" ")
def ordBurbuja(arreglo,longitud):
    for i in range(longitud):
        for j in range(longitud-i-1):
            if(arreglo[j]>arreglo[j+1]):
                aux=arreglo[j+1]
                arreglo[j+1]=arreglo[j]
                arreglo[j]=aux
def busquedaBinaria(arreglo,valor):
    izq = 0
    der = 0
    encontrado = False
    while(izq<=der and encontrado==False):
        medio=(izq+der)//2
        if(arreglo[medio]==valor):
            encontrado = True
        elif(arreglo[medio]<valor):
            izq=medio+1
        else:
            der=medio-1
    if(encontrado==True):
        print(f"El valor esta en la posicion {medio} ")
    else:
        print("El valor no esta en el arreglo")
def arreglo_a_matriz(matriz,filas,columnas,arreglo):
    indice=0
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = arreglo[indice]
            indice+=1
def main():

    filas=4
    columnas=4
    matriz=np.zeros([filas,columnas],dtype=int)

    # poner matriz en arreglo y ordenarlo, luego buscar un valor
    cargarMatriz(matriz,filas,columnas)
    mostrarMatriz(matriz,filas,columnas)
    longitud=filas*columnas
    # crear arreglo
    arreglo=np.zeros([longitud],dtype=int)
    matriz_a_Arreglo(matriz,filas,columnas,arreglo)
    print("Arreglo antes de ordenar; ")
    mostrarArreglo(arreglo,longitud)
    ordBurbuja(arreglo,longitud)
    print("\nArreglo ordenado: ")
    mostrarArreglo(arreglo,longitud)
    #busqueda binaria
    buscar=int(input("\ningresa un valor: "))
    busquedaBinaria(arreglo,buscar)
    #ordenar matriz
    arreglo_a_matriz(matriz,filas,columnas,arreglo)
    print("\nMatriz ordenada")
    mostrarMatriz(matriz,filas,columnas)
if __name__ == '__main__':
    main()