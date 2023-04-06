#Exercice 1
def verifie(t):
    for k in range(len(t)-1):
        if t[k]>t[k+1]:
            return False
    return True

print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))



#Exercice 2


def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
        liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale


Urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']
print(depouille(Urne))
print(vainqueur(depouille(Urne)))