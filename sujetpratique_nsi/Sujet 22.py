#Exercice 1

def liste_puissances(a,n):
    lp=[]
    nombre=a
    for k in range(1,n+1):
        for i in range(1,k):
            nombre*=a
        lp.append(nombre)
        nombre=a
    return lp

def liste_puissances_borne(a,n):
    lp=liste_puissances(a,n)
    for k in range(len(lp)):
        if lp[-1]>=n:
            lp.pop()
    return lp

print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puissances_borne(2, 16))
print(liste_puissances_borne(2, 17))
print(liste_puissances_borne(5, 5))

#Exercice 2

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,"G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,"M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,"R": 18, "S": 19, "T": 20, "U": 21, "V": 22,"W": 23, "X": 24, "Y": 25, "Z": 26}

def est_parfait(mot):
    # mot est une chaîne de caractères (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene%code_additionne==0:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

print(est_parfait("PAUL"))
print(est_parfait("ALAIN"))