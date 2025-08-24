import numpy as np
import math
n,m=map(int, input().split())
jugadores=np.zeros([n+1],dtype=int)
for i in range(m):
    x,y= map(int, input().split())
    elecciones= list(map(int,input().split()))
    k = elecciones.count(1)

    oroines1=math.floor(x/(k+1))
    oroines2=y

    if oroines1>=oroines2:
        print()
    else:
        print()

print(jugadores)