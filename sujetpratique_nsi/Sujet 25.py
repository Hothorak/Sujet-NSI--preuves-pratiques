#Exercice 1

def enumere(L):
    dic={e:[] for e in L}
    for k in range(len(L)):
        dic[L[k]].append(k)
    return dic
print(enumere([1, 1, 2, 3, 2, 1]))


#Exercice 2

class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste


def insere(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implémente
     un arbre binaire de recherche.
     """
    if arbre.v>cle:
        if arbre.fg is not None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd is not None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)

m=Arbre(5)
m.fg=Arbre(2)
m.fg.fd=Arbre(3)
m.fd=Arbre(7)
print(parcours(m,[]))
insere(m,1)
print(parcours(m,[]))
insere(m,4)
print(parcours(m,[]))
insere(m,6)
print(parcours(m,[]))
insere(m,8)
print(parcours(m,[]))