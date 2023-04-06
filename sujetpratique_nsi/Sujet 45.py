#Exercice 1

def rangement_valeurs(notes_eval):
    res=[0 for k in range(11)]
    for k in notes_eval:
        res[k]+=1
    return res

def notes_triees(t):
    res=[]
    for k in range(len(t)):
        for i in range(t[k]):
            res.append(k)
    return res

notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]

effectifs_notes = rangement_valeurs(notes_eval)
print(effectifs_notes)
print(notes_triees(effectifs_notes))

#Exercice 2

def dec_to_bin (nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

print(dec_to_bin(25))

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin == "1":
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit

print(bin_to_dec('101010'))

#intermediaire