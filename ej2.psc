Funcion cargarMatriz(matriz,filas,columnas)
	Definir i, j como entero
	Para i=0 hasta filas-1 Hacer
		para j=0 hasta columnas-1 hacer
			matriz[i,j] = azar(100)+1
		FinPara
	FinPara
FinFuncion

Funcion mostrarMatriz(matriz,filas,columnas)
	Definir i, j como entero
	Para i=0 hasta filas-1 Hacer
		para j=0 hasta columnas-1 hacer
			Escribir matriz[i,j]," | " Sin Saltar
		FinPara
		Escribir ""
	FinPara
FinFuncion

Algoritmo ej2
	//
	Definir matriz,filas,columnas Como Entero
	filas=7
	columnas=5
	Dimension matriz[filas,columnas]
	cargarMatriz(matriz,filas,columnas)
	//
	
	
	mostrarMatriz(matriz,filas,columnas)
FinAlgoritmo
