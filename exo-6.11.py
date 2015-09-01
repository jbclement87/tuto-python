print("entrez 3 longueur a, b et c ")
print("a :", end = "" )
a = int(input())
print("b : ", end = "" )
b = int(input())
print("c : ", end = "" )
c = int(input())

if a or b or c :
    print("on peu creer un triangle avec ces valeur")
else :
    print("on ne peux pas creer de triangle")
if (a == b) & (a == c) & (b == c):
    print("le triangle est equilatéral")
if (a == b) or (a == c) or (b == c):
    print("le triangle est isocèle")
if (a*a) == (b*b) + (c*c):
    print("le triangle est rectangle")
if (a != b) and (a!= c) and (b != c):
    print("le triangle est quelconque")
