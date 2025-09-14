Funcion busquedaBinaria(arreglo, n, valorcito)
	Definir izq, der,mid Como Entero
	Definir encontrado Como Logico
	encontrado=Falso
	izq=0
	der=n-1
	
	Mientras izq<=der  Y  no encontrado Hacer
		mid=trunc((izq+der)/2)
		si arreglo[mid]==valorcito Entonces
			encontrado=Verdadero
		SiNo
			si arreglo[mid]<valorcito Entonces
				izq=mid+1
			SiNo
				der=mid-1
			FinSi
		FinSi
	FinMientras
	
	si encontrado==Verdadero entonces
		Escribir "valor encontrado, en la posición: ", mid
	SiNo
		Escribir "valor no encontrado"
	FinSi
	
FinFuncion

Funcion cargarArreglo(arreglo)
	definir i como entero
	para i=0 Hasta 10-1 hacer
		arreglo[i]<-aleatorio(1,200)
	FinPara

FinFuncion

Funcion ordenar(arr,n)
	Definir i,j,tmp como entero
	n=n-1
	para i=0 hasta n-1 hacer
		para j=0 hasta n-i-1 hacer
			si arr[j]>arr[j+1] entonces
				tmp=arr[j+1]
				arr[j+1]=arr[j]
				arr[j]=tmp
			FinSi
		FinPara
	FinPara
FinFuncion

Funcion mostrarArreglo(arr)
	Definir  i Como Entero
	para i=1 Hasta 10-1 hacer
		escribir arr[i]," " sin saltar
		
	FinPara
FinFuncion

Algoritmo sin_titulo
	Definir arr, buscado, encontrado Como Entero
	Dimension arr[10]
	cargarArreglo(arr)
	ordenar(arr,10)
	mostrarArreglo(arr)
	Escribir ""
	Escribir "ingrese nro a buscar" Sin Saltar
	leer buscado
	busquedaBinaria(arr,10,buscado)
FinAlgoritmo
