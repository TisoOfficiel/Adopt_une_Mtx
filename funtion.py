from switch_fonction import *
import os 
import json
import csv
import datetime
from datetime import date

data_base_log={}
data_base_utilisateur={}
data_base_utilisateur_bonus={}
data_base_convertie={}
tuple_signe_astrologique_valeur=()
file_size = os.path.getsize(r'dict2.json') 
file_size2 = os.path.getsize(r'dict3.json') 
file_date_base_utilisateur = os.path.getsize(r'dict3.json')


def count_line():
    file = open("dict.txt", "r")
    reader = csv.reader(file)
    lines=len(list(reader))
    file.close()
    return lines


def fichier_vers_dico():
    global data_base_log
    global data_base_utilisateur_bonus
    global tuple_signe_astrologique_valeur
    with open("dict.txt","r",encoding="UTF-8") as f :
        id=0
        for line in f :
            id+=1
            line = line.strip()
            alist=line.split(',',12)
            data_base_utilisateur[id]={
                'Pseudo':alist[0],
                'Sexe':alist[1],
                'Date_de_Naissance' :alist[2],
                'Signe_Astrologie':alist[3],
                'Taille':alist[4],
                'Couleur_cheveux':alist[5],
                'Couleur_yeux':alist[6],
                'Sexe_rechercher':alist[7],
                'Age_rechercher':alist[8],
                'Taille_rechercher':alist[9],
                'Cheveux_rechercher':alist[10],
                'Yeux_rechercher':alist[11],
                'Questionnaire':alist[12]
            }
            data_base_convertie[id]={
                'Pseudo':alist[0],
                'Sexe':alist[1],
                'Date_de_Naissance' :alist[2],
                'Signe_Astrologie':alist[3],
                'Taille':alist[4],
                'Couleur_cheveux':alist[5],
                'Couleur_yeux':alist[6],
                'Sexe_rechercher':alist[7],
                'Age_rechercher':alist[8],
                'Taille_rechercher':alist[9],
                'Cheveux_rechercher':alist[10],
                'Yeux_rechercher':alist[11],
                'Questionnaire':alist[12]
            }

    if file_size ==0 : 
        data_base_log={}
    else : 
        with open('dict2.json',encoding="UTF-8") as json_file:
            data_base_log = json.load(json_file)

    if file_size2 ==0 : 
        data_base_utilisateur_bonus={}
    else : 
        with open('dict3.json',encoding="UTF-8") as json_file2:
            data_base_utilisateur_bonus = json.load(json_file2)
    

def dico_vers_fichier ():
    f = open("dict.txt","w+",encoding="UTF-8")
    y=[]
    for p_id in data_base_utilisateur:
        x =list(data_base_utilisateur[p_id].values())
        y.append(x)
            
    for i in y:
        z = str(i)
        z =z.replace("[","").replace("]","").replace(" ","").replace("'","")
        f.write(z+"\n")
    f.close()

    with open("dict2.json", "w+",encoding="utf-8") as file:
        json.dump(data_base_log, file,ensure_ascii=False)

    with open("dict3.json", "w+",encoding="utf-8") as file2:
        json.dump(data_base_utilisateur_bonus, file2,ensure_ascii=False)



def scan(pseudo):
    fichier_vers_dico()
    for i in data_base_utilisateur:
        if data_base_utilisateur[i]['Pseudo'] == pseudo.upper() :
            return True
    else :
        return False

def login_inscription (pseudo,mdp):
    i = len(data_base_log)+1 
    data_base_log[i]={}
    data_base_log[i]['Pseudo']= pseudo
    data_base_log[i]['Password']=mdp
    dico_vers_fichier()

def bio_photo_profile_inscription (pseudo,bio,photo_profile):
    global data_base_utilisateur_bonus
    i = len(data_base_utilisateur_bonus)+1 
    data_base_utilisateur_bonus[i]={}
    data_base_utilisateur_bonus[i]['Pseudo']= pseudo
    data_base_utilisateur_bonus[i]['Bio']= bio
    data_base_utilisateur_bonus[i]['Photo_Profile']=photo_profile
    dico_vers_fichier()

def inscription(pseudo,sexe,naissance,astrologie,taille,cheveux,yeux,sexe_rechercher,age_rechercher,taille_rechercher,cheveux_rechercher,yeux_rechercher,question1,question2,question3,question4,question5,question6,question7,question8,question9,question10):
    index = count_line()+1
    data_base_utilisateur[index]={}
    data_base_utilisateur[index]['Pseudo']= pseudo
    data_base_utilisateur[index]['Sexe']=switch_sexe(sexe)
    data_base_utilisateur[index]['Date_Naissance']=naissance
    data_base_utilisateur[index]['Signe_Astrologie']=switch_astrologie(astrologie)
    data_base_utilisateur[index]['Taille']=taille
    data_base_utilisateur[index]['Couleur_cheveux']=switch_couleur_cheveux(cheveux)
    data_base_utilisateur[index]['Couleur_yeux']=switch_couleur_yeux(yeux)
    data_base_utilisateur[index]['Sexe_rechercher'] = switch_sexe(sexe_rechercher)
    data_base_utilisateur[index]['Age_rechercher']=age_rechercher
    data_base_utilisateur[index]['Taille_rechercher']=taille_rechercher
    data_base_utilisateur[index]['Cheveux_rechercher']=switch_couleur_cheveux(cheveux_rechercher)
    data_base_utilisateur[index]['Yeux_rechercher']=switch_couleur_yeux(yeux_rechercher)
    data_base_utilisateur[index]['Questionnaire']=[question1,question2,question3,question4,question5,question6,question7,question8,question9,question10]
    
    dico_vers_fichier()
    
def data_base_utilisateur_vers_data_base_convertie():
    fichier_vers_dico()
    for i in data_base_convertie:
        data_base_convertie[i]['Sexe']=reverse_switch_sexe(data_base_utilisateur[i]['Sexe'])
        data_base_convertie[i]['Date_de_Naissance']= get_age(data_base_convertie[i]['Date_de_Naissance'])
        data_base_convertie[i]['Signe_Astrologie']=reverse_switch_astrologie(data_base_convertie[i]['Signe_Astrologie'])
        data_base_convertie[i]['Taille']=switch_taille(data_base_convertie[i]['Taille'])
        data_base_convertie[i]['Couleur_cheveux']=reverse_switch_couleur_cheveux(data_base_convertie[i]['Couleur_cheveux'])
        data_base_convertie[i]['Couleur_yeux']=reverse_switch_couleur_yeux(data_base_convertie[i]['Couleur_yeux'])
        data_base_convertie[i]['Sexe_rechercher'] = reverse_switch_sexe(data_base_convertie[i]['Sexe_rechercher'])
        data_base_convertie[i]['Age_rechercher']=switch_age_rechercher(data_base_convertie[i]['Age_rechercher'])
        data_base_convertie[i]['Taille_rechercher']=switch_taille(data_base_convertie[i]['Taille_rechercher'])
        data_base_convertie[i]['Cheveux_rechercher']=reverse_switch_couleur_cheveux(data_base_convertie[i]['Cheveux_rechercher'])
        data_base_convertie[i]['Yeux_rechercher']=reverse_switch_couleur_yeux( data_base_convertie[i]['Yeux_rechercher'])
        data_base_convertie[i]['Bio']=data_base_utilisateur_bonus[str(i)]["Bio"]
        data_base_convertie[i]['Photo_Profile']=data_base_utilisateur_bonus[str(i)]["Photo_Profile"]

def scan_connexion(pseudo,mdp):
    fichier_vers_dico()
    for i in data_base_log:
        if data_base_log[i]['Pseudo'] == pseudo and data_base_log[i]['Password']==mdp:
            return True
    return False

def get_age(argument):
    jour,mois,annee = argument.split('/')
    date_naissance =datetime.datetime(int(annee),int(mois),int(jour))
    annee,mois,jour = str(date.today()).split('-')
    date_actuel = datetime.datetime(int(annee),int(mois),int(jour))
    age = ((date_actuel.year - date_naissance.year) * 12 + (date_actuel.month - date_naissance.month))//12
    return str(age)

def scan_suppresion(pseudo):
   for i in data_base_utilisateur:
        if i<=len(data_base_utilisateur):
            if data_base_utilisateur[i]['Pseudo'].upper() == pseudo :
                identifiant = i
                return True,identifiant
        else :
            return False,"Suppression impossible"

def supprimer (pseudo):
    x,y=scan_suppresion(pseudo)
    if x:
        del data_base_utilisateur[y]
        del data_base_convertie[y]
        del data_base_log[str(y)]
        del data_base_utilisateur_bonus[str(y)]

        for id in range(y,len(data_base_utilisateur)+1):
            data_base_utilisateur[id] = data_base_utilisateur[id+1]
            del data_base_utilisateur[id+1]

        for id in range(y,len(data_base_convertie)+1):
            data_base_convertie[id] = data_base_convertie[id+1]
            del data_base_convertie[id+1]

        for id in range(y,len(data_base_log)+1):
            data_base_log[str(id)] = data_base_log[str(id+1)]
            del data_base_log[str(id+1)]

        for id in range(y,len(data_base_utilisateur_bonus)+1):
            data_base_utilisateur_bonus[str(id)] = data_base_utilisateur_bonus[str(id+1)]
            del data_base_utilisateur_bonus[str(id+1)]
    
        dico_vers_fichier()
        
    else : print(y)