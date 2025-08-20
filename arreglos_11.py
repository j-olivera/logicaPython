import numpy as np

arreglo = np.zeros([20],dtype=int)
bandera=0
for i in range(20):
    while True:
        n = int(input("Ingrese un numero: "))
        for j in range(20):
            if n==arreglo[j]:
                print("El numero ya se encuentra en el arreglo")
                bandera=1
            else:
                bandera=0
        if bandera==0:
            break
    arreglo[i]=n