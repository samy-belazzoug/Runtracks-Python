"""Job 1"""

def My_print_hello():
    return "Hello world" #Note : c'est une méthode pas une fonction car pas de return

My_print_hello()

"""Job 2"""

def My_print_name(name):
    return name

My_print_name("Samy")
My_print_name("Scott")
My_print_name("Frederic")

"""Job 3"""

def Add(a:int,b:int):
    return a + b

Add(4,5)
Add(10,2)
Add(10972,256)
Add(4,4)

"""job 4"""

def GetHello():
    return "Hello La Plateforme"

GetHello()

"""Job 5"""

def calcule(num1:float,operator:str,num2:float):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2
    if operator == "%":
        return num1 % num2

"""Job 6"""

def relatif(nombre):
    """if nombre >= 0:
        return "Positif"
    else:
        return "Négatif"""
    return nombre >= 0
    
#print(relatif(-1))

"""Job 7"""

def dev_type(language:str):
    if language == "JavaScript":
        print("tu es un développeur web")
    elif language == "python":
        print("tu es un développeur ia")
    elif language == "java":
        print("tu es un développeur logiciel")
    elif language == "reactjs":
        print("tu es un développeur mobile")
    else:
        print("un jour, je serais le meilleur développeur...")

"""Job 8"""

def saison_fruits(type:str,saison:str):
    if type == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    if type == "fruits" and saison == "été":
        return "poire, fraise et cassis"
    if type == "légume" and saison == "hiver":
        return "carotte, topinambour et endive"
    if type == "légume" and saison == "été":
        return "artichaut, aubergine, navet"

"""Job 9"""

def moyenne(note1,note2,note3):
    moyenne_etudiant = (note1 + note2 + note3) / 3
    if 15 <= moyenne_etudiant <= 20:
        print("Très bon élève")
    if 11 <= moyenne_etudiant <= 14:
        print("Bon élève")
    if 8 <= moyenne_etudiant <= 10:
        print("Elève moyen")
    if 0 <= moyenne_etudiant <= 7:
        print("Elève devant faire des efforts (pas bon...)")
    
#moyenne(1,20,13)

"""Job 10"""

def parite(nombre:int): #vérifie si le nombre est un entier
    if nombre < 0: #vérifie si le nombre est positif
        print("Veuillez saisir un entier positif.")
    else:
        return nombre % 2 == 0

#print(parite(-1))

"""Job 11"""

def time_to_text(nombre:int)->str:
    X = int(nombre / 60)
    Y = int(nombre % 60)
    return f"{X} heures et {Y} minutes."

#print(time_to_text(150))

"""Job 12"""

def inversion(chaine:str):
    s = ""
    i = -1
    while len(s) != len(chaine):
        s += chaine[i]
        i -= 1
    return s

#print(inversion("nikana"))

