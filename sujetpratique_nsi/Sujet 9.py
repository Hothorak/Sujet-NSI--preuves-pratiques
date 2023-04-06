#Exercice 1

def multiplication(n1,n2):
    res=0
    for k in range(abs(n2)):
        res+=n1
    if n1<0 and n2<0:
        return abs(res)
    return res

print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))

#Exercice 2

def chercher(tab, n, i, j):
    if i < 0 or j > len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2
    if tab[m] < n:
        return chercher(tab, n, m+1, j)
    elif tab[m] > n:
        return chercher(tab, n, i, m-1)
    else:
        return m
print()
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 6, 0, 5))