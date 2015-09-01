
liste = [32, 5, 12, 8, 3, 75, 2, 15]


i = 0

while i<len(liste):
    if liste[i] > liste[i+1]:
        if liste[i] < liste[i+1]:
            liste [i] = liste[i+1]
    i = i+1
    print("plus grand chiffre est" , liste[i])
