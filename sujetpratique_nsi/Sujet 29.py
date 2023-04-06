#Exercice 1

class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

a=Arbre(1)
a.fg=Arbre(4)
a.fd=Arbre(0)
a.fd.fd=Arbre(7)

b=Arbre(0)
b.fg=Arbre(1)
b.fg.fg=Arbre(3)
b.fd=Arbre(2)
b.fd.fg=Arbre(4)
b.fd.fg.fg=Arbre(6)
b.fd.fd=Arbre(5)

def taille(a):
    if a is None:
        return 0
    return 1 + taille(a.fd) + taille(a.fg)

def hauteur(a):
    if a is None:
        return 0
    return 1 + max(hauteur(a.fd), hauteur(a.fg))

print(taille(a))
print(hauteur(a))
print(taille(b))
print(hauteur(b))


#Exercice 2

def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice<nbre_elts:
        for i in range(indice):
            L[i] = liste[i]
        L[i+1] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[i+1] = element
    return L

print(ajoute(1, 4, [7, 8, 9]))
print(ajoute(3, 4, [7, 8, 9]))
print(ajoute(4, 4, [7, 8, 9]))
