from math import *

print("entrez une valeur : ", end = "")

v = int(input())

v = sqrt(v)
if v == 0 :
    print("impossible de calculer la racine carrée de la valeur")
else:
    print("la racine carrée est " , v)
