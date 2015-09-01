
def tableMulti(base, debut, fin):
    print('fragment de la table de multiplication par', base, ":")
    n= debut
    while n <= fin :
        print(n, "x" , base, "=" , n * base)
        n= n + 1

def table(base):
    resultat = []
    n = 1
    while n<  11:
        b = n * base
        resultat.append(b)
        n=n+1
    return resultat

def cube(n):
    return n**3

def volumeSphere(r):
    return 4 * 3.1416 * cube(r) / 3

r = input("entrez la valeur du rayon : ")
print("le volume de cette sphère vaut", volumeSphere(float(r)))