#Exercice 1

def recherche(caractere, chaine):
    oc=0
    for e in chaine:
        if e==caractere:
            oc+=1
    return oc

print(recherche('e', "sciences"))
print(recherche('i', "mississippi"))
print(recherche('a', "mississippi"))

#Exercice 2

valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre:
        return [v] + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang+1)

print()
print(rendu_glouton(67, 0))
print(rendu_glouton(291, 0))
print(rendu_glouton(291,1))

#Un peu galère le 2