print("veuillez entrer une valeur : " , end = " " )


liste = []
val = "truc"


while val != " ":
    val = input()
    liste.append(val)
    print("veuillez entrer une valeur : " , end = " " )
    if val == "":
        print(liste)



