"""Job 1"""
#Ecrire un programme qui parcourt les chiffres de 1 à 20

for i in range(0,21):
    #print(i)
    pass

i = 0
while i < 21:
    #print(i)
    i += 1

"""Job 2"""
#Ecrire un programme qui parcourt les chiffres de 1 à 20 mais affiche 1/2 nombres

for i in range(0,21): #Marche mais pas comme voulu dans l'exo
    if i%2:
        #print(i)
        pass

i = 0
while i < 21:
    #print(i)
    i += 2

"""Job 3"""
#Ecrire un programme qui parcourt les chiffres de 1 à 20 et affiche le carré de ces nombres

for i in range(0,21,2):
    #print(i)
    pass

i = 0
while i < 21:
    #print(i)
    #print(i**2)
    i += 1

"""Job 4"""
#Ecrire un programme qui affiche dans le Terminal les tables de multiplications de 1 à n (N étant un entier > 0 saisi par l'utilisateur)
"""
n = int(input("Entrez un entier strictement supérieur à 0 (N) : "))
k = 1
i = 0
"""
"""
while i < n:
    print("Table de multiplication de ",k)
    print(f"{k} × 1 = {k*1}")
    print(f"{k} × 2 = {k*2}") 
    print(f"{k} × 3 = {k*3}") 
    print(f"{k} × 4 = {k*4}" )
    print(f"{k} × 5 = {k*5}" )
    print(f"{k} × 6 = {k*6}" )
    print(f"{k} × 7 = {k*7}" )
    print(f"{k} × 8 = {k*8}" )
    print(f"{k} × 9 = {k*9}" )
    print(f"{k} × 10 = {k*10}")
    print("")
    k += 1
    i += 1
"""
#Demander à l'utilisateur

"""Job 5"""
"""
for N in range(1,13):
    print(N)"""
#Transformer cette boucle en for en boucle while pour obtenir le même résultat en console

N = 0
while N < 13:
    #print(N)
    N += 1

"""Job 6"""
"""
N = int(input("Saisissez le nombre de nombres de  :"))
i = 0
while N:
    pass
"""

"""Job 7"""

i = 1
while i < 13:
    #print(f"Tour {i}:",(i*3)-2)
    i += 1

"""Job 8"""
i = 2
k = 1
while k < 13:
    print(f"Tour {k}:",i)
    i += 2
    k += 1

"""Job 9"""
#afficher les nombres pairs et impairs de 1 à 30 à l'aide d'une boucle

impair = 1
pair = 0
while impair < 31 or pair < 31:
    print("Pair :",pair)
    print("Impair : ",impair)
    pair += 2
    impair += 2