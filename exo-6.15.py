liste = []
n = 0
a = 0
i = 0
k = 0
max = 0
min = 20
snote = 0
moyenne = 0


while a == 0 :
    print("entrez une note :" , end = "")
    n = int(input())
    liste.append(n)
    print("il y a " , len(liste), "note(s)")

    while i < len(liste):
        if liste[i] > max:
            max = liste[i]
        if liste [i] < min :
            min = liste[i]
        i = i + 1
    print("la note maximum est " , max)
    print("la note minimum est" , min)
    while k < len(liste):
        snote = snote + liste[k]
        moyenne = snote/len(liste)
        k = k + 1
    print("la moyenne des notes est " , moyenne )
    if n < a :
        a = a+1




