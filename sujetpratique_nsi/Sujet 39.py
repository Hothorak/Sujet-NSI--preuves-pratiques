#Exercice 1

def fibonacci(n):
    un=1
    u0=un
    u1=1
    for k in range(2,n):
        un+=u1
        u1=u0
        u0=un
    return un

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(25))
print(fibonacci(45))
print()

#Exercice 2

def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []
    for i in range(len(eleves)-1):
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]
    return (note_maxi, meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
print(pantheon(eleves_nsi, notes_nsi))
print(pantheon([],[]))