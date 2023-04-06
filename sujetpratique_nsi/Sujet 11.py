#Exercice 1

def convertir(tab):
    dic={0:128, 1:64, 2:32, 3:16, 4:8, 5:4, 6:2, 7:1}
    if len(tab)!=8:
        for k in range(8-len(tab)):
            tab.insert(0,0)
    compteur=0
    for k in range(len(tab)):
        if tab[k]==1:
            compteur+=dic[k]
    return compteur

print(convertir([1, 0, 1, 0, 0, 1, 1]))
print(convertir([1, 0, 0, 0, 0, 0, 1, 0]))


#Exercice 2

def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j - 1]
            j = j-1
        tab[j] = valeur_insertion


liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]
tri_insertion(liste)
print(liste)
