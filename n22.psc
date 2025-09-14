funcion cargarVector(arreglo,n)
	definir i Como Entero
	
	para i= 0 hasta n-1 hacer
		arreglo[i]=aleatorio(0,50)
	FinPara
FinFuncion

funcion mostrarVector(arreglo,n)
	definir i Como Entero
	
	para i=0 hasta n-1 hacer
		Escribir arreglo[i], " | " Sin Saltar
	FinPara
FinFuncion

Funcion IzqaDer(arreglo,n)
	definir i,j,aux Como Entero
	
	n=n-1
	
	para i = n-1 hasta 0 Con Paso -1 Hacer
		para j=0 hasta i Hacer
			si arreglo[j]>arreglo[j+1] entonces
				aux=arreglo[j]
				arreglo[j]=arreglo[j+1]
				arreglo[j+1]=aux
			FinSi
		FinPara
	FinPara
	
FinFuncion

funcion DeraIzq(arreglo,n)
	definir i,j,aux como entero
	n=n-1
	
	para i=0 hasta n-1 hacer
		para j=n hasta i+1 con paso -1 Hacer
			si arreglo[j-1] > arreglo[j] entonces
				aux=arreglo[j]
				arreglo[j]=arreglo[j-1]
				arreglo[j-1]=aux
			FinSi
		FinPara
	FinPara
FinFuncion

funcion sacudida(arreglo,n)
	Definir j,izq,der,aux Como Entero
	
	n=n-1
	izq=0
	der=n
	
	mientras izq < der Hacer
		para j=izq hasta der-1 Hacer
			si arreglo[j]>arreglo[j+1]Entonces
				aux=arreglo[j]
				arreglo[j]=arreglo[j+1]
				arreglo[j+1]=aux
			FinSi
		FinPara
		
		der=der-1
		
		para j=der hasta izq+1 Con Paso -1 Hacer
			si arreglo[j-1]>arreglo[j]Entonces
				aux=arreglo[j-1]
				arreglo[j-1]=arreglo[j]
				arreglo[j]=aux
			FinSi
		FinPara
		izq=izq+1
	FinMientras
FinFuncion

funcion TestCom(arreglo,n)
	Definir i,j,senial,aux Como Entero
	
	n=n-1
	senial=0
	i=0
	
	mientras i<= n-1 y senial == 0 Hacer
		senial=1
		
		para j=n hasta i+1 con paso -1 Hacer
			si arreglo[j-1]>arreglo[j] Entonces
				aux=arreglo[j-1]
				arreglo[j-1]=arreglo[j]
				arreglo[j]=aux
				
				senial=0
			FinSi
		FinPara
		i=i+1
	FinMientras
FinFuncion



Algoritmo sin_titulo
	definir arreglo como entero
	
	Dimension arreglo[6]
	
	cargarVector(arreglo,6)
	Escribir "Vector desordenado..."
	mostrarVector(arreglo,6)
	Escribir ""
	
	Escribir "Metodo de izq a der"
	IzqaDer(arreglo,6)
	mostrarVector(arreglo,6)
	Escribir ""
	
	Escribir "Metodo de der a izq"
	DeraIzq(arreglo,6)
	mostrarVector(arreglo,6)
	Escribir ""
	
	Escribir "Metodo Sacudida"
	sacudida(arreglo,6)
	mostrarVector(arreglo,6)
	Escribir ""
	
	Escribir "Metodo de Test de Comprobacion"
	TestCom(arreglo,6)
	mostrarVector(arreglo,6)
	Escribir ""
	
FinAlgoritmo
