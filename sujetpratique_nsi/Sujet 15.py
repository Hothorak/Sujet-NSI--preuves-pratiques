#Exercice 1

def mini(releve, date):
    minim=0
    for k in range(len(releve)):
        if releve[k]<releve[minim]:
            minim=k
    return (releve[minim], date[minim])

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(mini(t_moy, annees))

#Exercice 2

def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
        result = caractere+result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse==chaine

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

print(inverse_chaine('bac'))
print(est_palindrome('NSI'))
print(est_palindrome('ISN-NSI'))
print(est_nbre_palindrome(214312))
print(est_nbre_palindrome(213312))