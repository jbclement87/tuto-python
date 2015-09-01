liste = [32, 28, 41, 72, 22, 5, 12, 8, 3, 75, 2, 15]

i = 0

lp = []
li = []

while i < len(liste):
    if (liste[i] % 2 == 0 ):
        lp.append(liste[i])
    else :
        li.append(liste[i])
    i = i+1


print(lp)
print(li)


