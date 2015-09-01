t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
' Juillet ' , ' Août ' , ' Septembre ' , 'Octobre ' , ' Novembre ' , ' Décembre ' ]

a = 0
t3 = []

while a < len(t1):
    t3.append(t2[a])
    t3.append(t1[a])
    a = a+1

print(t3)

