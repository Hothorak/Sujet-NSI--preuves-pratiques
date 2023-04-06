#Exercice 1

def recherche(elt,tab):
    indice=-1
    for k in range(len(tab)):
        if elt==tab[k]:
            return k
    return indice

print(recherche(1, [2, 3, 4]))
print(recherche(1, [10, 12, 1, 56]))
print(recherche(50, [1, 50, 1]))
print(recherche(15, [8, 9, 10, 15]))
print(recherche(50, []))
print(recherche(4, [2, 4, 4, 3, 4]))

#Exercice 2

def insere(a, tab):
    l = list(tab)
    l.append(a)
    i = len(l) - 2
    while i >= 0 and a < tab[i]:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l

print(insere(3, [1, 2, 4, 5]))
print(insere(30, [1, 2, 7, 12, 14, 25]))
print(insere(1, [2, 3, 4]))
print(insere(1, []))