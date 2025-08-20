import math
def mcm(a,b):
    return abs(a*b)//math.gcd(a,b)

n_1=int(input("numerador: "))
d_1=int(input("denominador: "))
print(f"fraccion: {n_1}/{d_1}")

while True:

    n_2=int(input("numerador: "))
    d_2=int(input("denominador: "))
    print(f"fraccion: {n_2}/{d_2}")
    maximo_cm=mcm(d_1,d_2)
    n_n=maximo_cm/d_1*n_1+maximo_cm/d_2*n_2
    print(f"fraccion: {n_n}/{maximo_cm}")
    n_1=n_n
    d_1=maximo_cm

