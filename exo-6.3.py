#calcul de la periode d'un pendule
from math import *
print("entrez la longueur du pendule et la valeur d'acceleration")

l = float(input())
g = float(input())

t = 2*pi*sqrt(l/g)

print("la periode du pendule est" , t)