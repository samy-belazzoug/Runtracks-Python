"""Job 4"""

#print("abcdefghijklmonopqrstuvwxyz")

"""Job 5"""

#print("zyxwvutsrqponmlkjihgfedcba")

#alternative
def inversion_str(s:str)->str:
    """Ce programme inverse une chaine de caractères"""
    new_string = ""
    indentation = len(s) - 1
    while indentation >= 0:
        new_string += s[indentation]
        #print(indentation)
        indentation -= 1
    return new_string
#print(inversion_str("abcdefghijklmnopqrstuvwxyz"))

"""Job 6"""

ma_string = "Je suis une String"
#print(ma_string)

"""Job 7"""

num1 = 40
num2 = 2
#print(num1 + num2)

    #Job 8

num1 = 3
num2 = 14
#print(num1 * num2)

"""Job 9"""

produit1 = "Ferrari Daytona SP3"
prix_unitaire = 2250000
quantité_en_stock = 599

print("Nom : ",produit1,"\n""Prix (à l'unité): ",prix_unitaire,"\n""Stock disponible", quantité_en_stock)

quantité_en_stock += 75

#acheteur = int(input("Combien de Ferrari Daytona SP3 voulez vous acheter (Vous êtes riche hein) :"))
#quantité_en_stock -= acheteur
#print(quantité_en_stock)

inflation = 1.10
prix_unitaire *= inflation
#print(prix_unitaire)

#print("Nom : ",produit1,"\n""Prix (à l'unité): ",prix_unitaire,"\n""Stock disponible", quantité_en_stock)

"""Job 10"""

Montant_Initial_Investissement = 6500
Taux_Rendement_Annuel = 1.30

Montant_apres_investissement = Montant_Initial_Investissement * Taux_Rendement_Annuel
gain_annuel = (Montant_Initial_Investissement * Taux_Rendement_Annuel) - Montant_Initial_Investissement
print(Montant_Initial_Investissement, "->",Montant_apres_investissement," (",gain_annuel,")")
print(f"Nom : {produit1}\nPrix : {prix_unitaire}\nStock disponible : {quantité_en_stock}")

Montant_Initial_Investissement += 5000
Taux_Rendement_Annuel = 1.32
#print(Montant_Initial_Investissement*Taux_Rendement_Annuel)

Montant_Initial_Investissement *= 0.90
Taux_Rendement_Annuel = 1.31
print(Montant_Initial_Investissement*Taux_Rendement_Annuel)

"""Pour aller plus loin"""

s = "Salute toi"
print("e" in s)

x = "Hello"
y = "World"
print(x,y)

print(f"")

#QCM REPONSES : https://docs.google.com/forms/d/e/1FAIpQLSeIRtK65oU49SdJ_7K2UoPKBQ3MUrvD6L1x6KE3YAjmurtF0A/viewform?usp=pp_url&entry.1910084372=Un+conteneur+pour+stocker+une+valeur&entry.1719496140=print(my_str)&entry.1552474905=x+%3D+10&entry.858847196=variable_1&entry.1226125276=17&entry.149303964=Hello+World&entry.1240915853=tva+%3D+input(%22Saisissez+le+taux+de+TVA+:%22)&entry.893000223=nb_voitures+%3D+nb_voitures+%2B+2&entry.893000223=nb_voitures+%2B%3D+2&entry.453631737=total+*+1.1