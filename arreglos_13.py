# 13. Desarrollar un programa para cargar un matriz llamada valores de 5x5 y luego
#  Calcular la suma de todos los valores cargados en la matriz valores y
# mostrarlos.
#  Recorrer la matriz valores por fila o por columna buscando el mayor y el
# menor valor de la matriz y las posiciones en que se encuentran. Mostar los
# valores obtenidos.
#  Calcular el promedio de cada fila y guardar los resultados en un vector
# llamado promedioF.
#  Calcular el promedio de cada columna y guardar los resultados en un vector
# llamado promedioC.
import numpy as np
import random
matriz = np.zeros([5,5], dtype=int)
total=0
for i in range(5):
    for j in range(5):
        #matriz[i][j] = int(input(f"[{i+1}][{j+1}]: " )) # podes poner un acumulador aca o hacerlo luego
        matriz[i][j] = random.randint(0,20) # no quiero hacer pruebas
        total=matriz[i][j]
print(matriz,"\n")
menor=999
mayor=-1
index_menor_i=0
index_menor_j=0
index_mayor_i=0
index_mayor_j=0
for i in range(5):
    for j in range(5):
        if matriz[i][j]>mayor:
            mayor=matriz[i][j]
            index_mayor_j=j
            index_mayor_i=i
        if matriz[i][j]<menor:
            menor=matriz[i][j]
            index_menor_i=i
            index_menor_j=j
print(f"menor: {menor} - pos: i-{index_menor_i} j-{index_menor_j}")
print(f"mayor: {mayor} - pos: i-{index_mayor_i} j-{index_mayor_j}")

promedioF = np.zeros([5],dtype=int)
tmp=0
for i in range(5):
    for j in range(5):
        tmp+=matriz[i][j] # i -> j se reccore primero las por columna, es decir recorre una fila
    promedioF[i]=tmp/5
    tmp=0

print(promedioF,"\n")

promedioC = np.zeros([5],dtype=int)
tmp=0
for i in range(5):
    for j in range(5):
        tmp+=matriz[j][i] # i -> j se reccore primero las por columna, es decir recorre una fila
    promedioC[i]=tmp/5
    tmp=0
print(promedioC,"\n")
    