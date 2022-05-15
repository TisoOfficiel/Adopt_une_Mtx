from compatibilite_function import * 
from funtion import fichier_vers_dico,data_base_utilisateur
fichier_vers_dico()

def compatibilite_personne1_vers_tous(Personne1):
    list_resultat_compatible_avec_taux=[]
    genre(Personne1)
    for i in list_personne_compatible:
        resultat =resultat = 100-(compatibilite_age(identifiant_personne1,i[0])+compatibilite_signe_astrologique(identifiant_personne1,i[0])+compatibilité_chemin_de_vie(identifiant_personne1,i[0])+compatibilite_autre_critere(identifiant_personne1,i[0])+questionnaire(identifiant_personne1,i[0]))
        list_resultat_compatible_avec_taux.append([i[1],resultat])
    return tri(list_resultat_compatible_avec_taux)

#Fonction compatibilité en fonction du sexe/sexe rechercher entre la personne entré et le reste des inscrits de l'appli
def genre(personne1):
    list_identifiant_personne=[]
    global list_personne_compatible
    #Augmentation de la porter
    global identifiant_personne1
    list_personne_compatible=[]
    #Boucle for pour trouver le genre et genre rechercher de la personne voulut et ajour dans une liste tout les autres membres de l'application
    for i in data_base_utilisateur:
        if data_base_utilisateur[i]["Pseudo"]==personne1:
            sexe_personne1=data_base_utilisateur[i]["Sexe"]
            sexe_personne1_rechercher=data_base_utilisateur[i]["Sexe_rechercher"]
            identifiant_personne1=i
        else : 
            list_identifiant_personne.append(i)
    #Dans la liste contenant tous les membres,récupération du sexe et sexe rechercher et comparaison avec la personne donné puis si compatible ajout dans une nouvelle liste
    for i in list_identifiant_personne:
        sexe_personne2=data_base_utilisateur[i]["Sexe"]
        sexe_personne2_rechercher=data_base_utilisateur[i]["Sexe_rechercher"]
            
        if sexe_personne1_rechercher==sexe_personne2 and sexe_personne2_rechercher==sexe_personne1:
            list_personne_compatible.append([i,data_base_utilisateur[i]["Pseudo"]])

#Fonction tri avec en parametre la liste contenant toute les personnes compatibles
def tri(list):
    #On trie la liste par ordre croissant des valeurs de compatibilités puis on inverse pour avoir l'ordre décroissant
    list_trie_par_ordre_decroissant = sorted(list,key=lambda list: list[1],reverse=True)
    
    return list_trie_par_ordre_decroissant
