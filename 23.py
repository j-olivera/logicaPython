import random
from tkinter import W
import numpy as np

def cargarVector(vector,n):
	for i in range(n):
		vector[i]=random.randint(0,100)
	
		
def mostrarVector(vector,n):
	for i in range(n):
		print(vector[i]," | ",end="")
		
def ordenarVector(vector,n):
	for i in range(n):
		for j in range(n-i-1):
			if(vector[j]>vector[j+1]):
				aux=vector[j]
				vector[j]=vector[j+1]
				vector[j+1]=aux

		
def busquedaBinaria(vector,n,val):
	izq=0
	der=n-1 #longitud - 1
	while (izq<=der):
		medio = (izq+der)//2
		if(vector[medio]==val):
			return medio+1
		elif(vector[medio]<val):
			izq=medio+1
		else:
			der=medio-1
	return -1


				


vector=np.zeros([10],int)
	
	
cargarVector(vector,10)
	
print("Vector desordenado....")
mostrarVector(vector,10)
	
print("")
	
print( "vector ordenado....")
ordenarVector(vector,10)
mostrarVector(vector,10)

print("")
	
valbuscado=int(input("Ingrese el valor a buscar: "))
buscado=busquedaBinaria(vector,10,valbuscado)
if(buscado!=-1):
	print("Elemento encontrado en la posicion ",buscado)
else:
	print("Elemento no encontrado")
	
