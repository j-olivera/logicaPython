import numpy as np

matriz = np.zeros([3,4],dtype=int)

for i in range(3):
    for j in range(4):
        while True:
            a = int(input("Ingrese un numero entre el 0 y 9: "))
            if(a<0 or a>9):
                print("Numero no valido")
            else:
                break
        matriz[i][j]=a
for i in range(3):
    sumatoria=0
    for j in range(4):
        sumatoria+=matriz[i][j]
    print(f"Sumatoria fila {i+1}: {sumatoria}")

for j in range(4):
    producto=1
    for i in range(3):
        producto*=matriz[i][j]
    print(f"Producto de la columna {j+1}: {producto}")

print(matriz)