#Exercice 1

from random import *

def lancer(n):
    t=[]
    for k in range(n):
       t.append(randint(1,6))
    return t

def paire_6(tab):
    compteur=0
    for e in tab:
        if e==6:
            compteur+=1
    return compteur>=2

lancer1 = lancer(5)
lancer2 = lancer(5)
print(lancer1)
print(paire_6(lancer1))
print(lancer2)
print(paire_6(lancer2))
lancer3 = lancer(3)
print(lancer3)
print(paire_6(lancer3))
lancer4 = lancer(0)
print(lancer4)
print(paire_6(lancer4))

#Exercice 2

def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)


def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le négatif de l'image sous la forme
     d'une liste de listes'''
    # on créé une image de 0 aux mêmes dimensions que le paramètre
    image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = abs(image[i][j]-255)
    return L

def binaire(image, seuil):
    '''renvoie une image binarisée de l'image sous la forme
     d'une liste de listes contenant des 0 si la valeur
     du pixel est strictement inférieure au seuil
     et 1 sinon'''
    # on crée une image de 0 aux mêmes dimensions que le paramètre
    image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L


img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174,
207, 25, 87], [255, 0, 24, 197, 189]]

print(nbLig(img))
print(nbCol(img))
print(negatif(img))
print(binaire(img,120))
