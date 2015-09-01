print("quelle année ? : ", end="")

annee = int(input())

if annee % 4 == 0 :
    print("année bissextile")
if annee % 100 == 0:
    print("année normale")
if annee % 400 == 0:
        print("année bissextile")
else:
    print("année normale")

