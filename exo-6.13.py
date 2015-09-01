print("entrez la note : ", end="")

n = int(input())


if n >= 80:
    print("la note est A")
if n < 80 & n > 60:
    print("la note est B")
if n < 60 & n > 50:
    print("la note est C")
if n < 50 & n > 40:
    print("la note est D")
if n < 40:
    print("la note est E")
