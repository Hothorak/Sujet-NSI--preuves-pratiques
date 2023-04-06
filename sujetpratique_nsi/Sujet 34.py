#Exercice 1

def moyenne(tab):
    if len(tab)==0:
        return str("Non noté")
    note=0
    for e in tab:
        note+=e
    return note/len(tab)

print(moyenne([5, 3, 8]))
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(moyenne([]))

#Exercice 2

def tri(tab):
    # i est le premier indice de la zone non triée,
    # j est le dernier indice de cette zone non triée.
    # Au début, la zone non triée est le tableau complet.
    i = 0
    j = len(tab)-1
    while i != j:
        if tab[i] == 0:
            i = i+1
        else:
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur
            j = j-1
    return tab

print(tri([0, 1, 0, 1, 0, 1, 0, 1, 0]))

#Simple