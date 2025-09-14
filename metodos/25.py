import numpy as np
import random

from numpy.ma.core import indices
from sympy import trunc


def cargarCampos(camposZ,campos,zonas):
    for i in range(campos):
        for j in range(zonas):
            camposZ[i][j] = random.randint(0,500)


def promedioLluviasCampo(camposZ, campos, zonas, promediosC):
    for i in range(campos):
        acumulador = 0
        for j in range(zonas):
            acumulador += camposZ[i][j]
        promedio = acumulador / campos
        promediosC[i] = promedio


def promedioLluviasZona(camposZ, campos, zonas, promediosZ):
    for j in range(zonas):
        acumulador = 0
        for i in range(campos):
            acumulador += camposZ[i][j]
        promedio = acumulador / zonas
        promediosZ[j] = promedio


def mayoresLluvias(camposZ, campos, zonas,promediosMay):
    for i in range(campos):
        mayor=camposZ[i][0]
        for j in range(zonas):
            if(camposZ[i][j]>mayor):
                mayor = camposZ[i][j]
        promediosMay[i] = mayor

def verResultados(camposZ, campos, zonas, promediosZ, promediosC,promediosMay):
    #Matriz
    print("Campos y zonas ")
    for i in range(campos):
        for j in range(zonas):
            print(camposZ[i][j], end=" ")
        print("")
    print("Promedio de lluvias por campo ")
    for i in range(campos):
        print(promediosC[i], end=" ")
    print("\nPromedio de lluvias por zona")
    for i in range(zonas):
        print(promediosZ[i], end=" ")
    print("\nMayores promedios de lluvia por campo")
    for i in range(campos):
        print(promediosMay[i], end=" ")


def main():
    #
    datosCargados=False
    while True:
        print("""
        Opción 1 – Configuración del estudio a realizar
        Opción 2 - Cargar promedios de lluvia. 
        Opción 3 - Promedio de lluvias por campo
        Opción 4 - Promedio de lluvias por zona. 
        Opción 5 - Campo y zona con mayor promedio de lluvias
        Opción 6 – Ver resultados. 
        Opción 7 – Salir.
        """)
        op =  int(input("Ingresa una opcion: "))
        if op == 1:
            campos = int(input("Ingresa una cantidad de campos: "))
            zonas = int(input("Ingresa una cantidad de zonas por campo: "))
            camposZ = np.zeros([campos,zonas],dtype=int)
            promediosC = np.zeros([campos], dtype=int)
            promediosZ = np.zeros([zonas], dtype=int)
            promediosMay = np.zeros([campos], dtype=int)
            datosCargados = True
            #
        elif op == 2:
            if(datosCargados):
                cargarCampos(camposZ,campos,zonas)
            else:
                print("Debe cargar los datos..")
        elif op == 3:
            if(datosCargados):

                promedioLluviasCampo(camposZ,campos,zonas,promediosC)
            else:
                print("Debe cargar los datos..")
        elif op == 4:
            if(datosCargados):

                promedioLluviasZona(camposZ,campos,zonas,promediosZ)
            else:
                print("Debe cargar los datos..")
        elif op == 5:
            if(datosCargados):
                mayoresLluvias(camposZ,campos,zonas,promediosMay)
            else:
                print("Debe cargar los datos..")
        elif op == 6:
            if(datosCargados):
                verResultados(camposZ,campos,zonas,promediosZ,promediosC,promediosMay)
        elif op == 7:
            print("Saliendo...")
            break
        else:
            print("Ingrese una opcion valida")

if __name__ == '__main__':
    main()