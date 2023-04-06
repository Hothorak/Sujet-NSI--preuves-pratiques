#Exercice 1

def nombre_de_mots(p):
    compteur=0
    for k in range(len(p)):
        if p[k]==' ':
            if p[k+1]!='!' or p[k+1]!='?':
                compteur+=1
        if p[k]=='.':
            compteur+=1
            break
    return compteur

print(nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Le point d exclamation est separe !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))

#Exercice 2

class Noeud:

    def __init__(self, valeur):
        '''Méthode constructeur pour la classe Noeud.
        Paramètre d'entrée : valeur (int)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def getValeur(self):
        '''Méthode accesseur pour obtenir la valeur du noeud
            Aucun paramètre en entrée'''
        return self.valeur

    def droitExiste(self):
        '''Méthode renvoyant True si le sous-arbre droit est non
           vide
            Aucun paramètre en entrée'''
        return (self.droit is not None)

    def gaucheExiste(self):
        '''Méthode renvoyant True si le sous-arbre gauche est non
           vide
            Aucun paramètre en entrée'''
        return (self.gauche is not None)

    def inserer(self, cle):
        '''Méthode d'insertion de clé dans un arbre binaire de recherche Paramètre d'entrée : cle (int)'''
        if cle < self.valeur:
            # on insère à gauche
            if self.gaucheExiste():
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            if self.droitExiste():
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)


arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

print()
print(arbre.gauche.getValeur())
print(arbre.droit.getValeur())
print(arbre.gauche.gauche.getValeur())
print(arbre.gauche.droit.getValeur())


#ez