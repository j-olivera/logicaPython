import random 
import numpy as np

def cargarNumeros(arreglo):
    for i in range(50):
        arreglo[i] = random.randint(0,101)
        print(f"Nro de loteria - jugador N° {i+1} : {arreglo[i]}")

def sorteo(arreglo):
    n = random.randint(0,101)
    contador = 0
    print("Numero sorteado: ",n)
    for i in range(50):
        if arreglo[i] == n:
            print(f"Numero {i+1} ganaste la loteria")
            contador+=1
    if contador==0:
        print("No hubo ganadores")

def main():
    participantes = np.zeros([50],dtype=int)
    cargarNumeros(participantes)
    sorteo(participantes)

main()