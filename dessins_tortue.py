from turtle import *

def carre(taille , couleur, angle) :
    "fonction qui dessine un carré de taille et de couleur déterminées"
    color(couleur)
    left(angle)
    c=0
    while c<4:
        forward(taille)
        right(90)
        c=c+1

def triangle(taille, couleur, angle):
    color(couleur)
    left(angle)
    c=0
    while c<3:
        forward(taille)
        left(120)
        c=c+1

def etoile5(taille , couleur):
    color(couleur)
    c = 0
    while c<5:
        forward(taille)
        right(144)
        c= c+1

