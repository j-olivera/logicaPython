Algoritmo sin_titulo
	Definir m,i,j Como Entero
	Dimension m[5,5]
	Para i=0 hasta 5-1 Hacer
		para j=0 hasta 5-1 Hacer
			si i==0 o i==5-1 Entonces
				m[i,j]=1
			SiNo
				si j==0 o j==5-1 Entonces
					m[i,j]=1
				SiNo
					m[i,j]=0
				FinSi
			FinSi
		FinPara
	FinPara
	Para i=0 hasta 5-1 Hacer
		para j=0 hasta 5-1 Hacer
			Escribir m[i,j], " " Sin Saltar
		FinPara
		Escribir ""
	FinPara
FinAlgoritmo
