Funcion cargarVector(vector,n)
	definir i Como Entero
	
	para i =0 Hasta n-1 Hacer
		vector[i]=Aleatorio(0,100)
	FinPara
FinFuncion


Funcion mostrarVector(vector,n)
	Definir i Como Entero
	
	para i = 0 Hasta n-1 Hacer
		Escribir vector[i]," | " Sin Saltar
	FinPara
FinFuncion


funcion ordenarVector(vector,n)
	definir i,j,aux Como Entero
	para i =0 Hasta n-1 Hacer
		aux=vector[i]
		j=i-1
		
		mientras ((j>=0) y (vector[j] > aux)) Hacer
			vector[j+1]= vector[j]
			j=j-1
		FinMientras
		vector[j+1]=aux
	FinPara
FinFuncion


Funcion busquedaBinaria(vector,n,val)
	
	
	
	
	Definir izq,der,medio Como Entero
	Dimension arreglo[10]
	
	izq=0
	der=n-1

	medio = trunc((izq+der)/2)
	
	
	Mientras (izq <= der) y (vector[medio] <> val) Hacer
		Si  (val < vector[medio]) entonces
			der = medio - 1
		SiNo
			izq = medio + 1
		FinSi
		medio = trunc((izq+der)/2)
	FinMientras
	Si val = vector[medio] entonces
		Escribir "Elemento encontrado en la posición ",medio+1
	SiNo
		Escribir "Elemento no encontrado"
	FinSi

	
FinFuncion


Algoritmo sin_titulo
	definir vector,valbuscado Como Entero
	Dimension vector[10]
	
	
	cargarVector(vector,10)
	
	Escribir "Vector desordenado...."
	mostrarVector(vector,10)
	
	Escribir ""
	
	
	Escribir "vector ordenado...."
	ordenarVector(vector,10)
	mostrarVector(vector,10)
	
	Escribir ""
	
	Escribir "Ingrese el valor a buscar: "Sin Saltar
	leer valbuscado
	
	busquedaBinaria(vector,10,valbuscado)
	
FinAlgoritmo
