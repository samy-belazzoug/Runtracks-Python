"""Job 1"""

def liste()->list:
    fruits = ["pomme","cerise","orange"]
    return fruits
#print(liste())

"""Job 2"""

def liste2()->list:
    fruits = ["pomme","cerise","orange"]
    return fruits[1]
#print(liste2())

"""Job 4"""

def liste3()->list:
    fruits = ["pomme","cerise","orange"]
    fruits.append("Melon")
    return fruits
#print(liste3())

"""Job 4"""

def liste4()->list:
    fruits = ["pomme","cerise","orange"]
    fruits.insert(2,"mangue")
    return fruits
#print(liste4())

"""Job 5"""

L = [1,2,3,4,5]
#print(L)
#print(L[1])
def voisins(list):
    list[3] = list[2] + list[4]
    return list
#print(voisins(L))
#print(L[-1])

"""Job 6"""

l = [1,2,3,4,5]
l[0],l[-1] = l[-1],l[0]
#print(l)

"""Job 7"""

L = [8,24,48,2,16]
#print([x for x in L if x % 3 == 0])

"""Job 8"""

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
somme = 0
for element in L:
    if element % 2 == 0:
        somme += element
#print(somme)

"""Job 9"""

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
max = L[0]
min = L[0]
for element in L:
    if element >= max:
        max = element
    if element <= min:
        min = element
#print(f"la valeur max est : {max}""\n"f"la valeur min est : {min}")    

"""Job 10"""

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
produit = 1         #attention a pas mettre 0 car sinon le produit sera toujours égal à 0.
for element in L:
    if 25 <= element <= 90:
        produit *= element
#print(produit)

"""Job 11"""

L = [7, 11, 42, 39, 2]
#print([x + 1 for x in L])

"""Job 12"""

def longueur(liste): #Je fais cette fonction car on a pas le droit à len()
    compteur = 0
    for element in liste:
        if element:
            compteur += 1
    return compteur

def triage(l:list):
    i = 0
    j = 1
    while j < longueur(l):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
        else:
            pass
        i += 1
        j += 1
    return l

#print(triage([2,5,3,4,10,12,11]))
# doit renvoyer [2,3,4,5,10,11,12]

"""Job 13"""

def supp_doublons(l:list)->list:
    s = []
    for x in l:
        if not x in s:
            s.append(x) #Casse tête car pas le droit mais c'est la vie tu néco
    return s

print(supp_doublons([10, 20,30, 20, 10, 50, 60, 40, 80, 50, 40]))
# doit renvoyer [10,20,30,50,60,80,40]

"""Job 14"""

def my_long_word(n:int,s:str)->str:
    pass

print(my_long_word(3,"La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))