from dessins_tortue import *

up()
goto(-150,50)

i = 0
while i<10:
    down()
    carre(20, 'red')
    up()
    forward(30)
    i = i +1
a= input()