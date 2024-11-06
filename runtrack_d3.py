"""Job 1"""

"""
valeur1 = input("Saisir valeur : ")
valeur2 = input("Saisir valeur : ")

if valeur1 == valeur2:
    print("Valeur1 est égale à valeur2")
else:
    print("Les deux valeurs ne sont pas égales")
"""

"""Job 2"""

"""
age = int(input("Saisir votre âge"))
if age >= 18:
    print("Tu peux voter.")
else:
    print("Tu ne peux pas voter.")
"""

"""Job 3"""
"""
for i in range(101):
    if i == 26 or i == 37 or i == 88:
        pass
    else:
        print(i)
"""
"""Job 4"""

"""
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
"""

"""Job 5"""

"""
for i in range(2,1000):
    if i == 2 or i == 3 or i == 5 or i == 7:
        print(i)
    if i%2 == 0:
        pass
    elif i%3 == 0:
        pass
    elif i%4 == 0:
        pass
    elif i%5 == 0:
        pass
    elif i%6 == 0:
        pass
    elif i%7 == 0:
        pass
    elif i%8 == 0:
        pass
    elif i%9 == 0:
        pass
    else:
        print(i)
"""

"""Job 6"""
"""
nombre = int(input("Saisir un nombre entier : "))
if nombre % 2 == 0:
    print("Ce nombre est pair")
else:
    print("Ce nombre n'est pas pair")
"""

"""Job 7 JE LE HAIS ARRRRRRRRHHHHHHHHHHHHHH""" 

chaine = "abcdefghijklmnopqrstuvwxyz"*10
"""
i = 1
d = 0
while i <= len(chaine):
    print(chaine[d:i])
    i += 2
"""
"""Job 8"""

"""
 A
B C
"""
AC = int(input("Longueur coté A : "))
AB = int(input("Longueur coté B : "))
BC = int(input("Longueur coté C : "))

if AC > AB + BC:
    print("Impossible de construire ce triangle")
elif AB > AC + BC:
    print("Impossible de construire ce triangle")
elif BC > AB + AC:
    print("Impossible de construire ce triangle")

else:
    print("Triangle possible !")

if AC == AB == BC:
    print("Ce triangle est équilatéral.")
if AC == AB or AB == BC  or BC == AC:
    print("Ce triangle est isocèle.") 
if AC**2 == AB**2 + BC**2:
    print("Ce triangle est rectangle")
elif  AC != AB != BC:
    print("Ce triangle est quelquonque")