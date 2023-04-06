#Exercice 1

a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]


def ou_exclusif(t1,t2):
    tab=[]
    for k in range(len(t1)):
        if t1[k]==1 or t2[k]==1:
            if t1[k]==1 and t2[k]==1:
                tab.append(0)
            else:
                tab.append(1)
        else:
            tab.append(0)
    return tab

print(ou_exclusif(a,b))
print(ou_exclusif(c,d))

#Exercice 2

class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for
                        j in range(n)]

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)
        # test de la somme de chaque ligne
        for i in range(len(self.tableau)):
            if self.somme_ligne(i) != s:
                return False
        # test de la somme de chaque colonne
        for j in range(len(self.tableau[0])):
            if self.somme_col(j) != s:
                return False
        return True

liste = (3, 4, 5, 4, 4, 4, 5, 4, 3)
c3 = Carre(liste, 3)
print()
c3.affiche()
print(c3.est_semimagique())

liste= (1,7,7,1)
c2 = Carre(liste,2)
print()
c2.affiche()
print(c2.est_semimagique())

liste= (2,9,4,7,0,3,6,1,8)
c3bis = Carre(liste,3)
print()
c3bis.affiche()
print(c3bis.est_semimagique())

#intérmaidiraitre
