import numpy as np
def cargarEspectadores(cine):
    for i in range(0,7):
        print(f"Sala {i+1}.")
        for j in range(0,5):
            cine[i][j]=int(input(f"P{j+1}: "))

def mejorCombinacion(cine):
    sala=0 #revisar
    pelicula=0
    mejor=-1
    for i in range(0,7):
        for j in range(0,5):
            if cine[i][j]>mejor:
                sala=i
                pelicula=j
                mejor=cine[i][j]
    print("Mejor combinacion sala/pelicula")
    print(f"Sala N°{sala+1} - Pelicula N°{j+1}")
    print(f"Cantidad espectadores: {cine[sala][pelicula]}")

def masVista(cine):
    masVista=-1 
    columna=0
    for j in range(0,5):
        total=0
        for i in range(0,7):
            total+=cine[i][j]
        if total>masVista:
            masVista=total
            columna=j
    print(f"La pelicula mas vista es la pelicula N°{columna+1}: {masVista} total de espectadores")

def totalxSala(cine):
    
    for i in range(0,7):
        total=0
        for j in range(0,5):
            total+=cine[i][j]
        print(f"Sala {i+1}: {total} |")

def totalxPelicula(cine):
    for j in range(0,5):
        total=0
        for i in range(0,7):
            total+=cine[i][j]
        print(f"Pelicula N°{j+1}: {total}")

def main():
    cine = np.zeros([7,5], dtype=int)
    cargarEspectadores(cine)
    mejorCombinacion(cine)
    masVista(cine)
    totalxSala(cine)
    totalxPelicula(cine)

main()
