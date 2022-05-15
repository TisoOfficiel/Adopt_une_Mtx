from compatibilite_function import *
from funtion import fichier_vers_dico

fichier_vers_dico()

def compatibilite_entre_deux_personne (Pseudo1,Pseudo2):
    
    compatible_genre,identifiant_personne1,identifiant_personne2 = compatibilite_genre_entre_deux_personne(Pseudo1,Pseudo2)
    if compatible_genre == True:
        resultat = 100-(compatibilite_age(identifiant_personne1,identifiant_personne2)+compatibilite_signe_astrologique(identifiant_personne1,identifiant_personne2)+compatibilité_chemin_de_vie(identifiant_personne1,identifiant_personne2)+compatibilite_autre_critere(identifiant_personne1,identifiant_personne2)+questionnaire(identifiant_personne1,identifiant_personne2))
        return "Le taux de compatibilité entre "+Pseudo1+" et "+Pseudo2+" est de : "+str(resultat)+"%"
    else:
        data_base_utilisateur_vers_data_base_convertie()
        return "Impossible car pas les mêmes rechercher de genre"


#Fonction compatibilité en fonction de leur sexe et sexe recherché respectif:
def compatibilite_genre_entre_deux_personne(personne1,personne2):
    #Porter accessible pour toutes les autres fonctions
    global identifiant_personne1,identifiant_personne2
    
    #Creation des variables
    personne1_trouver=personne2_trouver=False
    sexe_personne1=""
    sexe_personne1_rechercher=""
    sexe_personne2=""
    sexe_personne2_rechercher=""
    
    for i in data_base_utilisateur:
        #On sort de la boucle si les deux personnes sont trouver
        if personne1_trouver==personne2_trouver and personne1_trouver==True:
            break
        else : 
            if data_base_utilisateur[i]["Pseudo"]==personne1:
                sexe_personne1=data_base_utilisateur[i]["Sexe"]
                sexe_personne1_rechercher=data_base_utilisateur[i]["Sexe_rechercher"]
                identifiant_personne1=i
                personne1_trouver =True    
            if data_base_utilisateur[i]["Pseudo"]==personne2:
                sexe_personne2=data_base_utilisateur[i]["Sexe"]
                sexe_personne2_rechercher=data_base_utilisateur[i]["Sexe_rechercher"]
                identifiant_personne2=i
                personne1_trouver=True
    #Comparaison mutuelle des sexe et des sexes rechercher
    if sexe_personne1_rechercher==sexe_personne2 and sexe_personne2_rechercher==sexe_personne1:
        return True,identifiant_personne1,identifiant_personne2
    else: 
        return False,identifiant_personne1,identifiant_personne2
