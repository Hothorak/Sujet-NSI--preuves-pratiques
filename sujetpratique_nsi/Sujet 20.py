#Exercice 1

def ajoute_dictionnaires(d1,d2):
    dic={}
    for k in d1:
        dic[k]=d1[k]
    for i in d2:
        if i in dic:
            dic[i]+=d2[i]
        else:
            dic[i]=d2[i]
    return dic

print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({}, {2: 9, 3: 11}))
print(ajoute_dictionnaires({1: 5, 2: 7}, {}))

#Exercice 2

from random import randint

def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while nbre_cases > len(cases_vues):
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n = n + 1
    return n

print(nbre_coups())
