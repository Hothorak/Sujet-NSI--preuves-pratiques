#Exercice 1

def ecriture_binaire_entier_positif(n):
    res=[]
    if n ==0 :
        return [0]
    while n!=0:
        b = n%2
        n=n//2
        res.append(b)
    res.reverse()
    return res

print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))

#Pas au programme