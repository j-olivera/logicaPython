# El director de le Escuela de Ingeniería de la UNdeC requiere determinar con
# urgencia aquellos alumnos que cursan más de una carrera de ingeniería relacionada con
# sistemas. Dispone del número de DNI de todos los alumnos de cada carrera de sistemas
# de la escuela. Se solicita diseñar un programa que permita cargar los documentos de los
# alumnos de las carreras de Ing. en Sistemas e Ing. Mecatrónica en una matriz llamada
# alIngenierias de 2x20 elementos y luego determine aquellos alumnos comunes a ambas
# carreras. Estos alumnos se guardarán en un nuevo arreglo llamado alumnosC de 20
# elementos y se mostrarán en pantalla. 

import numpy as np
import random
alumnos = np.zeros([2,20],dtype=int)
alumnosc = np.zeros([20],dtype=int)

for i in range(2):
    for j in range(20):
        alumnos[i][j]= random.randint(0,9) # simula el dni

print(alumnos)
for i in range(1):
    for j in range(20):
        if alumnos[i][j]==alumnos[i+1][j]: #al ser dos filas, con un solo recorrido mas sumar 1 al index se recorren las dos al mismo tiempo
            alumnosc[j]=alumnos[i][j]
# mostrar los alumnos
for i in range(20):
    if alumnosc[i]!=0:
        print(alumnosc[i])


