#Retourne un chiffre entier en fonction du sexe en parametre
def switch_sexe (argument):
    return{
        "Homme" : "1",
        "Femme" : "2",
        "Non Binaire":"3",
    }.get(argument,"Sexe introuvable")

#Retourne un chiffre entier en fonction du signe astrologique en parametre
def switch_astrologie(argument):
    return {
        "Belier": "1",
        "Taureau": "2",
        "Gemeaux": "3",
        "Cancer": "4",
        "Lion": "5",
        "Vierge": "6",
        "Balance": "7",
        "Scorpion": "8",
        "Sagitaire": "9",
        "Capricorne": "10",
        "Verseau": "11",
        "Poission": "12",
    }.get(argument, "Signe Astroligue invalide")

#Retourne un chiffre entier en fonction de la couleur des cheveux en parametre
def switch_couleur_cheveux(argument):
    return {
        "Noirs": "1",
        "Châtains": "2",
        "Blonds": "3",
        "Roux": "4",
        "Gris": "5",
        "Blancs": "6",
    }.get(argument, "Couleur de cheveux invalide")

#Retourne un chiffre entier en fonction de la couleur des yeux en parametre
def switch_couleur_yeux(argument):
    return {
        "Noirs": "1",
        "Marrons": "2",
        "Verts": "3",
        "Bleus": "4",
        "Gris": "5",
    }.get(argument, "Couleur de cheveux invalide")

#Retourne le sexe en fonction du chiffre entier en parametre
def reverse_switch_sexe (argument):
    return{
        "1" : "Homme",
        "2" : "Femme",
        "3":"Non Binaire",
    }.get(argument,"Sexe introuvable")

#Retourne le signe astrologique en fonction du chiffre entier en parametre
def reverse_switch_astrologie(argument):
    return {
        "1": "Belier",
        "2": "Taureau",
        "3": "Gemeaux",
        "4": "Cancer",
        "5": "Lion",
        "6": "Vierge",
        "7": "Balance",
        "8": "Scorpion",
        "9": "Sagitaire",
        "10": "Capricorne",
        "11": "Verseau",
        "12": "Poission",
    }.get(argument, "Signe Astroligue invalide")

#Retourne la couleur de cheveux en fonction du chiffre entier en parametre   
def reverse_switch_couleur_cheveux(argument):
    return {
        "1": "Noirs",
        "2": "Châtains",
        "3": "Blonds",
        "4": "Roux",
        "5": "Gris",
        "6": "Blancs",
    }.get(argument, "Couleur de cheveux invalide")

#Retourne la couleur des yeux en fonction du chiffre entier en parametre
def reverse_switch_couleur_yeux(argument):
    return {
        "1": "Noirs",
        "2": "Marrons",
        "3": "Verts",
        "4": "Bleus",
        "5": "Gris",
    }.get(argument, "Couleur de cheveux invalide")

#Retourne la taille en fonction du chiffre entier en parametre
def switch_taille(argument):
    return {
        "1": "< 1,50m",
        "2": "entre 1,50m et 1,60m",
        "3": "entre 1,60m et 1,70m",
        "4": "entre 1,70m et 1,80m",
        "5": "entre 1,80m et 1,90m",
        "6": "> 1,90m",
    }.get(argument, "Taille invalide")

#Retourne une tranche d'âge en fonction du chiffre entier en parametre
def switch_age_rechercher (argument):
    return {
        "1": "18 - 24",
        "2": "25 - 30",
        "3": "31 - 40",
        "4": "41 - 50",
        "5": "51 - 60",
        "6": "61 -  +",
    }.get(argument, "Age rechercher invalide")