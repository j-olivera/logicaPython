import numpy as np
import random

def cargarDatos(arr):
    for i in range(6):
        arr[i]=random.randint(1,6)

def burbuja(arr):
    for i in range(6):
        for j in range(6-i-1):
            if(arr[j]>arr[j+1]):
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp

arr=np.zeros([6])
cargarDatos(arr)
print("arreglo original")
print(arr)
print("arreglo ordenado")
burbuja(arr)
print(arr)