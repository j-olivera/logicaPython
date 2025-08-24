xmin=0
xmax=0
ymin=0
ymax=0
equis=[]
yes=[]
n=int(input("Ingresa la cantidad de ñires:"))
for i in range(n):
    x=int(input("x: "))
    equis.append(x)
    y=int(input("y: "))
    yes.append(y)
equis.sort()
yes.sort()
xmin=equis[0]
ymin=yes[0]
xmax=equis[n-1]
ymax=yes[n-1]
perimetro = 2 * ((xmax-xmin+2)+(ymax-ymin+2))
print("Perimetro: ",perimetro)