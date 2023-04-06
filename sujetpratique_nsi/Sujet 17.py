#Exercice 1

def moyenne(liste_notes):
    n=0
    c=0
    for e in liste_notes:
        n1,c1=e
        n+=n1*c1
        c+=c1
    return n/c

print(moyenne([(15, 2), (9, 1), (12, 3)]))

#Exercice 2

def pascal(n):
    triangle = [[1]]
    for k in range(1, n-1):
        ligne_k = [k]
        for i in range(1, k):
            ligne_k.append(triangle[k-1][i - 1] + triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle

print(pascal(4))
print(pascal(5))
