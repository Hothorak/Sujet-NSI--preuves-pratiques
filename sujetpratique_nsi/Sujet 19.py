#Exercice 1

def recherche(tab,n):
    g=0
    d=len(tab)
    for k in range(len(tab)):
        if g>d:
            return -1
        m=(g+d)//2
        if tab[m]>n:
            d=m-1
        elif tab[m]<n:
            g=m+1
        else:
            return m
    return -1

print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))

#Exercice 2

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c)+decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat


print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
print(cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5))