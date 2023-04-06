#Exercice 1

def renverse(mot):
    fin=""
    for e in mot:
        fin= e+fin
    return fin

print(renverse("informatique"))

#Exercice 2

def crible(n):
    """
     Renvoie un tableau contenant tous les nombres premiers plus petits
     que n
     """
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(0, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2 * i, n, i):
                tab[multiple] = False
    return premiers

print(crible(40))


#simple