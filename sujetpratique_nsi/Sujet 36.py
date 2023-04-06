#Exercice 1

def couples_consecutifs(tab):
    """Fonction qui renvoie des couples consécutifs dans tab"""
    assert len(tab)!=0,'la liste est vide'
    res=[]
    for k in range(len(tab)-1):
        if tab[k]-tab[k+1] == -1:
            res.append((tab[k],tab[k+1]))
    return res

print(couples_consecutifs([1, 4, 3, 5]))
print(couples_consecutifs([1, 4, 5, 3]))
print(couples_consecutifs([1, 1, 2, 4]))
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
print(couples_consecutifs ([5, 1, 2, 3, 8, -5, -4, 7]))

#Exercice 2

def propager(M, i, j, val):
    if M[i][j] == 1:
        M[i][j] = val
    # l'élément en haut fait partie de la composante
    if i - 1 >= 0 and M[i - 1][j] == 1:
        propager(M, i - 1, j, val)
    # l'élément en bas fait partie de la composante
    if i+1 < len(M) and M[i + 1][j] == 1:
        propager(M, i+1, j, val)
    # l'élément à gauche fait partie de la composante
    if j - 1 >= 0 and M[i][j + 1] == 1:
        propager(M, i, j-1, val)
    # l'élément à droite fait partie de la composante
    if j+1 < len(M) and M[i][j+1] == 1:
        propager(M, i, j+1, val)

M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
propager(M, 2, 1, 3)
print()
for e in M:
    print(e)

#inter
