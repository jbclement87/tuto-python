from turtle import *



def triangle(couleur):
    """

    :rtype : object
    """
    a = 0
    while a<3:
        color(couleur)
        forward(100)
        left(120)
        a = a+1

def cercle(couleur):
    b = 0
    while b<20:
        color(couleur)
        forward(30)
        left(30)
        b= b+1

triangle("blue")
up()
forward(200)
down()
triangle("green")
up()
left(90)
forward(300)
down()
cercle("red")
