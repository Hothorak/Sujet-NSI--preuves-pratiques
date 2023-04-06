#Exercice 1

def fusion(tab1,tab2):
    tab=[]
    max=len(tab1)+len(tab2)
    while len(tab)!=max:
        if len(tab1)==0:
            tab.append(tab2.pop(0))
        elif len(tab2)==0:
            tab.append(tab1.pop(0))
        elif tab1[0]<=tab2[0]:
            tab.append(tab1.pop(0))
        elif tab1[0]>tab2[0]:
            tab.append(tab2.pop(0))
    return tab

print(fusion([3, 5], [2, 5]))
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))

#Exercice 2

romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}


def traduire_romain(nombre):
    """ Renvoie l’écriture décimale du nombre donné en chiffres
    romains """
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]]:
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]


print(traduire_romain("XIV"))
print(traduire_romain("CXLII"))
print(traduire_romain("MMXXIII"))