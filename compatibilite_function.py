import json
from funtion import *
with open('dict4.json') as json_file3:
    tuple_signe_astrologique_valeur = tuple(json.load(json_file3))
#Transforme l'age rechercher en value en fonction de la tranche d'age
def switch_age_value(argument):
    x = 6
    result = 1
    i=24
    while i < 61:
        if argument <=i :
            argument =result
            break
        result +=1
        i+=x
        x=10
    return result

#Fonction compatibilité age :
def compatibilite_age (identifiant1,identifiant2):
    data_base_utilisateur_vers_data_base_convertie()
    age_personne1=switch_age_value(int(data_base_convertie[identifiant1]["Date_de_Naissance"]))
    age_personne1_rechercher=int(data_base_utilisateur[identifiant1]["Age_rechercher"])
    age_personne2=switch_age_value(int(data_base_convertie[identifiant2]["Date_de_Naissance"]))
    age_personne2_rechercher=int(data_base_utilisateur[identifiant2]["Age_rechercher"])
    resultat=abs((age_personne1_rechercher-age_personne2)+(age_personne2_rechercher-age_personne1))       
    return resultat

#Fonction compatibilité signe astrologique:
def compatibilite_signe_astrologique(identifiant1,identifiant2):
    #Soustraction de 1 pour commencer directement a l'index 0 lors de la recheche dans le tuple
    signe_astrologique_personne1=int(data_base_utilisateur[identifiant1]["Signe_Astrologie"])-1
    signe_astrologique_personne2=int(data_base_utilisateur[identifiant2]["Signe_Astrologie"])-1

    #Comparaison pour toujour avoir la plus petite valeur dans la variable ligne
    if signe_astrologique_personne1 > signe_astrologique_personne2 : 
        ligne,colonne=signe_astrologique_personne2,signe_astrologique_personne1
    else : ligne,colonne=signe_astrologique_personne1,signe_astrologique_personne2

    #Selection dans le cas ou les deux personnes sont des poissons car pas de tuple imbriquer dans ce cas uniquement
    if ligne==colonne and ligne==11:
        result =10- (tuple_signe_astrologique_valeur[ligne]//10) #Division de la valeur par 10 pour avoir un chiffre et puis soustraction sur 10 pour inverser les valeurs de sorte a que un gros score donne un écart faible
    else :
        result =10- (tuple_signe_astrologique_valeur[ligne][colonne-ligne]//10)
    return result


#Fonction compatibilité chemin de vie 
def compatibilité_chemin_de_vie(identifiant1,identifiant2):
    #Creation d'une liste contenant pour chaque cellule un élément de la date de naissance
    date_de_naissance_personne1=data_base_utilisateur[identifiant1]["Date_de_Naissance"].split("/")
    date_de_naissance_personne2=data_base_utilisateur[identifiant2]["Date_de_Naissance"].split("/")

    #Conversion au type int pour faire des calculs
    date_de_naissance_convertie_personne1= int(date_de_naissance_personne1[0])+int(date_de_naissance_personne1[1])+int(date_de_naissance_personne1[2])
    date_de_naissance_convertie_personne2=int(date_de_naissance_personne2[0])+int(date_de_naissance_personne2[1])+int(date_de_naissance_personne2[2])


    while date_de_naissance_convertie_personne1 > 1 :
        if date_de_naissance_convertie_personne1 >=1 and date_de_naissance_convertie_personne1<=9 :
            break
        else : 
            #Conversion au format string afins de pouvoir manipuler chaque caratère
            date_de_naissance_convertie_personne1=str(date_de_naissance_convertie_personne1)
            resultat_liste_date_de_naissance=[]

            for i in range(len(date_de_naissance_convertie_personne1)):
                #Remplissage de la liste pour chaque caratère sous format interger
                resultat_liste_date_de_naissance.append(int(date_de_naissance_convertie_personne1[i]))
            #reinitialisation de la variable afin de la réutiliser
            date_de_naissance_convertie_personne1=0
            for i in range(len(resultat_liste_date_de_naissance)):
                #Addition de chaque valeur de la liste pour faire un seul chiffre
                date_de_naissance_convertie_personne1+=resultat_liste_date_de_naissance[i]
    #Meme chose mais pour la personne 2
    while date_de_naissance_convertie_personne2 > 1 :
        if date_de_naissance_convertie_personne2 >=1 and date_de_naissance_convertie_personne2<=9 :
            break
        else : 
            date_de_naissance_convertie_personne2=str(date_de_naissance_convertie_personne2)
            resultat_liste_date_de_naissance=[]
            for i in range(len(date_de_naissance_convertie_personne2)):
                resultat_liste_date_de_naissance.append(int(date_de_naissance_convertie_personne2[i]))
            date_de_naissance_convertie_personne2=0
            for i in range(len(resultat_liste_date_de_naissance)):
                date_de_naissance_convertie_personne2+=resultat_liste_date_de_naissance[i]
    result=abs(date_de_naissance_convertie_personne1-date_de_naissance_convertie_personne2)
    return result

#Fonction compatibilité concernant les autres critères:
def compatibilite_autre_critere(identifiant1,identifiant2):
    
    taille_personne1=int(data_base_utilisateur[identifiant1]["Taille"])
    taille_personne1_rechercher=int(data_base_utilisateur[identifiant1]["Taille_rechercher"])
    couleur_yeux_personne1=int(data_base_utilisateur[identifiant1]["Couleur_yeux"])
    couleur_yeux_personne1_rechercher=int(data_base_utilisateur[identifiant1]["Yeux_rechercher"])
    couleur_de_cheuveux_personne1=int(data_base_utilisateur[identifiant1]["Couleur_cheveux"])
    couleur_de_cheveux_personne1_rechercher=int(data_base_utilisateur[identifiant1]["Cheveux_rechercher"])


    taille_personne2=int(data_base_utilisateur[identifiant2]["Taille"])
    taille_personne2_rechercher=int(data_base_utilisateur[identifiant2]["Taille_rechercher"])
    couleur_yeux_personne2=int(data_base_utilisateur[identifiant2]["Couleur_yeux"])
    couleur_yeux_personne_rechercher2=int(data_base_utilisateur[identifiant2]["Yeux_rechercher"])
    couleur_de_cheveux_personne2=int(data_base_utilisateur[identifiant2]["Couleur_cheveux"])
    couleur_de_cheveux_personne2_rechercher=int(data_base_utilisateur[identifiant2]["Cheveux_rechercher"])

    resultat_recherche_personne1_vers_personne2=abs((taille_personne1_rechercher-taille_personne2)+(couleur_yeux_personne1_rechercher-couleur_yeux_personne2)+(couleur_de_cheveux_personne1_rechercher-couleur_de_cheveux_personne2))
    resultat_recherche_personne2_vers_personne1=abs((taille_personne2_rechercher-taille_personne1)+(couleur_yeux_personne_rechercher2-couleur_yeux_personne1)+(couleur_de_cheveux_personne2_rechercher-couleur_de_cheuveux_personne1))
    result = resultat_recherche_personne1_vers_personne2+resultat_recherche_personne2_vers_personne1
    return result

#Fonction compatibilité questionnaire:
def questionnaire(identifiant1,identifiant2):
    #creation de la variable result, initialisé à 0
    result =0
    #Attribution au variables les réponses du questionnaire
    questionnaire1=data_base_utilisateur[identifiant1]["Questionnaire"].split(",")
                
    questionnaire2=data_base_utilisateur[identifiant2]["Questionnaire"].split(",")

    for i in range(len(questionnaire1)):
        result+=abs(int(questionnaire1[i])-int(questionnaire2[i]))
    
    return result


