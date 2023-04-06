#Exercice 1

def recherche_indices_classement(elt,tab):
    t1=[]
    t2=[]
    t3=[]
    for k in range(len(tab)):
        if tab[k]<elt:
            t1.append(k)
        elif tab[k]==elt:
            t2.append(k)
        else:
            t3.append(k)
    return t1,t2,t3

print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
print(recherche_indices_classement(3, [1, 1, 1, 1]))
print(recherche_indices_classement(3, []))

#Exercice 2

def moyenne(nom, dico_result):
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return -1