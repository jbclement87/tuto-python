from math import *

print("entrez les valeur des coté du triangles : ")

a = float(input())
b = float(input())
c = float(input())

d = (a+b+c) /2
calcul = d*(d-a)*(d-b)*(d-c)
aire = sqrt(calcul)

print("l'aire du triangle est " , aire)