import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from funtion import *
from compatibilite_deux_personnes import *
from PIL import Image, ImageTk
from compatibilite_1_vers_tous import *

root=tk.Tk()

def show_frame(frame):
    frame.tkraise()

#Liste 
list_phrase_accueil = ["Bienvenue sur ","Welcome to ","Willkommen zu ","Bienvenido a ","欢迎来到 ","Bem-vindo ao ","Benvenuto a "]
list_phrase_devise = ["L'amour n'attends que vous","Love is waiting for you","Liebe wartet auf dich","El amor te esta esperando","爱在等你","O amor está esperando por você","L'amore ti sta aspettando"]


i=0 # Index de la liste initiliasité à 0
var_accueil = StringVar()
var_devise = StringVar()
var_accueil.set(list_phrase_accueil[0]+"Adopte un•e MTX ")
var_devise.set(list_phrase_devise[0])

#Fontion 

def Connexion():
    result= scan_connexion(identifiant_entre.get().upper(),identifiant_mot_de_passe.get())
    if result :
        messagebox.showinfo("Connexion Réussite", "Connexion réussite, bienvenue parmis nous "+ identifiant_entre.get())
        show_frame(page_main),affichage()
    else :
        messagebox.showwarning("Connexion Impossible", "Erreur vérifier votre Identifiant et Mot de passe")

def creation_compte():
    global filename
    if scan(entre_pseudo.get())==True :
        messagebox.showwarning("Problème identifiant","Impossible de vous inscrire car votre Pseudo à déja été pris")
    else : 
        login_inscription(entre_pseudo.get().upper(),entre_mot_de_passe.get())
        inscription(entre_pseudo.get().upper(),liste_sexe.get(),entre_date_de_naissance.get(),liste_signe_astrologie.get(),taille_selection.get(),liste_couleur_cheveux.get(),liste_couleur_yeux.get(),liste_sexe_rechercher.get(),age_selection.get(),taille_rechercher_selection.get(),liste_couleur_cheveux_rechercher.get(),liste_couleur_yeux_rechercher.get(),var_question1.get(),var_question2.get(),var_question3.get(),var_question4.get(),var_question5.get(),var_question6.get(),var_question7.get(),var_question8.get(),var_question9.get(),var_question10.get())
        bio_photo_profile_inscription(entre_pseudo.get().upper(),texte_description.get(1.0,END).strip(),os.path.relpath(filename))
        boutton_envoyer2.configure(state="active")
        
def changement_titre_devise():        
        global i 
        i+=1
        var_accueil.set(list_phrase_accueil[i]+"Adopte un•e MTX ")
        var_devise.set(list_phrase_devise[i])
        if i< len(list_phrase_accueil)-1 :
            root.after(4000, changement_titre_devise)  # reschedule event in 2 seconds
        else :
            i=-1
            root.after(4000, changement_titre_devise)

def HidePassword ():
    if identifiant_mot_de_passe['show']=="*":
        identifiant_mot_de_passe['show']=""
    else : identifiant_mot_de_passe['show']="*"

root.geometry('965x965')#définit la taille de la fenêtre
root.rowconfigure(0,weight=1)#La grille se fera sur une largeur de une ligne
root.columnconfigure(0,weight=1)#La grille se fera sur une largeur de une colonne


page_accueil=tk.Frame(root,bg='#008BFF')#creation de la page d'accueil
page_login=tk.Frame(root,bg='#008BFF')#creation de la page connexion 
page_inscription=tk.Frame(root)#creation de la page inscription
page_main=tk.Frame(root)#creation de la frame/boite accueil
page_compatibilite_deux=tk.Frame(root)
#pour les frames dans la list (...) les frames crée seront la ligne 0 avec la colonne0 centrée
for frame in (page_accueil,page_login,page_inscription,page_main,page_compatibilite_deux): 
    frame.grid(row=0,column=0,sticky='NESW')


#Code pour la page d'accueil
frame_conteneur=tk.Frame(page_accueil,bg='#008BFF')
frame_conteneur.pack(expand=YES)

frame_menu_navigation=tk.Frame(page_accueil,bg='#008BFF',pady=50)
frame_menu_navigation.pack(side=BOTTOM)


label_text_accueil = tk.Label(frame_conteneur, textvariable=var_accueil, font = ('Arial 45 '),bg="#008BFF",fg='white')
label_text_accueil.pack()
label_text_devise = tk.Label(frame_conteneur, textvariable=var_devise, font = ('Arial 25 italic'),bg="#008BFF",fg="white")
label_text_devise.pack()

bouton_continuer = tk.Button(frame_menu_navigation,text="Continuer",font = ('Helvetica 20 italic'),command=lambda:show_frame(page_login))
bouton_continuer.pack()



"""----------------------------------------------------------------------------------------------------------------
 page_accueil_btn=tk.Button(frame_menu_navigation,text='Suppresion',command=lambda:show_frame(page_login))
 page_accueil_btn.grid(row=0,column=0)
 page_login_btn=tk.Button(frame_menu_navigation,text='Affichage',command=lambda:show_frame(page_inscription))
 page_login_btn.grid(row=0,column=1)
----------------------------------------------------------------------------------------------------------------"""

#Code pour la page Connexion

frame_conteneur=tk.Frame(page_login,bg='#008BFF')
frame_conteneur.pack(expand=YES)

frame_menu_navigation=tk.Frame(page_login,bg='#008BFF',pady=50)
frame_menu_navigation.pack(side=BOTTOM)

label_text_login = tk.Label(frame_conteneur, text="Veuillez-vous connecter ou bien vous inscrire", font = ('Arial 20 '),bg="#008BFF",fg='white')
label_text_login.pack(expand=YES)

label_identifiant=tk.Label(frame_conteneur, text="Identifiant",font = "Arial 15",bg="#008BFF",fg='black',pady=10,padx=5)
label_identifiant.pack(side=LEFT)

identifiant_entre = tk.Entry(frame_conteneur,width=50,)
identifiant_entre.pack(side=LEFT)

label_mot_de_passe=tk.Label(frame_conteneur, text="Mot de passe",font = "Arial 15",bg="#008BFF",fg='black',pady=10,padx=5)
label_mot_de_passe.pack(side=LEFT)

identifiant_mot_de_passe = tk.Entry(frame_conteneur,width=50,show="*")
identifiant_mot_de_passe.pack(side=LEFT)

button_afficher_mdp=Button(frame_conteneur,text="Afficher le mdp",command=HidePassword)
button_afficher_mdp.pack()
bouton_connexion = tk.Button(frame_menu_navigation,text="Connexion",font = ('Helvetica 20 italic'),command=Connexion)
bouton_connexion.pack(side=LEFT)

bouton_creation_compte = tk.Button(frame_menu_navigation,text="S'incrire",font = ('Helvetica 20 italic'),command=lambda:show_frame(page_inscription))
bouton_creation_compte.pack(side=LEFT)





#Code pour la page Inscription

frame0=tk.Frame(page_inscription,)
frame0.pack(fill="x")
frame1=tk.Frame(page_inscription)
frame1.pack()
frame2=tk.Frame(page_inscription,)
frame2.pack()
frame3=tk.Frame(page_inscription,)
frame3.pack()


label_top =Label(frame0,text="INSCRIPTION",font=('Helvetica 30'))
label_top.pack(pady=1)

label_frame1 = LabelFrame(frame1,text="Vos informations personnel",labelanchor='n',padx=5,pady=5,font=('Helvetica 20'))
label_frame1.grid(row=0,column=0,padx=5)

label_frame2 = LabelFrame(frame1,text="Vous recherchez",labelanchor='n',padx=46,pady=15,font=('Helvetica 20'))
label_frame2.grid(row=0,column=1,padx=5)

label_frame3 = LabelFrame(frame2,text="Questionnaire",padx=27,font=('Helvetica 20'))
label_frame3.grid(row=1,columnspan=2,padx=5)

label_frame4= LabelFrame(frame3,text="Ajouter une petite bio",font=('Helvetica 20'))
label_frame4.grid(row=2,column=0)

label_frame5= LabelFrame(frame3,text="Ajouter une photo de profile",font=('Helvetica 20'))
label_frame5.grid(row=2,column=1,padx=25)

#Pseudo 
label_pseudo = Label(label_frame1,text="Identifiant / Pseudo :",font=('Helvetica 12'))
label_pseudo.grid(row=0,column=0,sticky="W")
entre_pseudo=Entry(label_frame1,width=25)
entre_pseudo.grid(row=0,column=1)

#Mot de passe 
label_mot_de_passe=Label(label_frame1,text="Mot de passe :",font=('Helvetica 12'))
label_mot_de_passe.grid(row=1,column=0,sticky="W")
entre_mot_de_passe=Entry(label_frame1,width=25)
entre_mot_de_passe.grid(row=1,column=1)

#Date de naissance
label_date_de_naissance=Label(label_frame1,text="Date de naissance format (JJ/MM/AAAA) :",font=('Helvetica 12'))
label_date_de_naissance.grid(row=3,column=0,sticky="W")
entre_date_de_naissance=Entry(label_frame1,width=25)
entre_date_de_naissance.grid(row=3,column=1)

#Sexe
label_sexe=Label(label_frame1,text="Sexe :",font=('Helvetica 12'))
label_sexe.grid(row=4,column=0,sticky="W")
liste_sexe = ttk.Combobox(label_frame1,text="Liste",values=["Homme","Femme","Non Binaire"],state="readonly",width=22)
liste_sexe.grid(row=4,column=1,)

#Signe Astrologique
label_signe_astro=Label(label_frame1,text="Signe Astrologique :",font=('Helvetica 12'))
label_signe_astro.grid(row=5,column=0,sticky="W")
liste_signe_astrologie=ttk.Combobox(label_frame1,values=["Belier","Taureau","Gemeaux","Cancer","Lion","Vierge","Balance","Scorpion","Sagitaire","Capricorne","Verseau","Poisson"],state="readonly",width=22)
liste_signe_astrologie.grid(row=5,column=1)

#Taille 
label_taille=Label(label_frame1,text="Taille :",font=('Helvetica 12'))
label_taille.grid(row=8,column=0,sticky="W")
radio_taille = (('< 1,50m', 1),('entre 1,50m et 1,60m', 2),('entre 1,60m et 1,70m', 3),('entre 1,70m et 1,80m', 4),('entre 1,80m et 1,90m', 5),
        ('> 1,90m', 6))
taille_selection = StringVar()    
b = -1
for r in range(3):
   for c in range(2):
        b = b+1
        radiobtn =Radiobutton(label_frame1,text=radio_taille[b][0],value=radio_taille[b][1], variable=taille_selection,font=('Helvetica 10'))
        radiobtn.grid(row=9+r,column=c,sticky='W')

#Couleur de Cheveux
label_cheveux=Label(label_frame1,text="Couleur de cheveux: ",font=('Helvetica 12'))
label_cheveux.grid(row=12,column=0,sticky="W",)
liste_couleur_cheveux =ttk.Combobox(label_frame1,values=["Noirs","Châtains","Blonds","Roux","Gris","Blanc"],state="readonly",width=22)
liste_couleur_cheveux.grid(row=12,column=1)

#Couleur de Yeux 
label_yeux=Label(label_frame1,text="Couleur des yeux: ",font=('Helvetica 12'))
label_yeux.grid(row=13,column=0,sticky="W")
liste_couleur_yeux=ttk.Combobox(label_frame1,values=["Noirs","Marrons","Verts","Bleus","Gris"],state="readonly",width=22)
liste_couleur_yeux.grid(row=13,column=1,)


#Ce que que vous rechercher --------------------------------------------------------------------

#Sexe 
label_sexe_rechercher = Label(label_frame2,text="Sexe",font=('Helvetica 12'))
label_sexe_rechercher.grid(row=0,column=0,sticky="W")
liste_sexe_rechercher =ttk.Combobox(label_frame2,values=["Homme","Femme","Non Binaire",],state="readonly",width=22)
liste_sexe_rechercher.grid(row=0,column=1)

#Age 
label_age_rechercher=Label(label_frame2,text="Age :",font=('Helvetica 12'))
label_age_rechercher.grid(row=1,column=0,sticky="W")
radio_age = (('18 - 24', 1),('25 - 30', 2),('31 - 40', 3),('41 - 50', 4),('51 - 60', 5),
        ('61 -  +', 6))
age_selection = StringVar()    
b = -1
for r in range(2):
   for c in range(3):
        b = b+1
        radiobtn =Radiobutton(label_frame2,text=radio_age[b][0],value=radio_age[b][1], variable=age_selection,font=('Helvetica 10'))
        radiobtn.grid(row=2+r,column=c,)

#Taille 
label_taille_rechercher=Label(label_frame2,text="Taille :",font=('Helvetica 12'))
label_taille_rechercher.grid(row=4,column=0,sticky="W")
radio_taille_rechercher = (('< 1,50m', 1),('entre 1,50m et 1,60m', 2),('entre 1,60m et 1,70m', 3),('entre 1,70m et 1,80m', 4),('entre 1,80m et 1,90m', 5),
        ('> 1,90m', 6))
taille_rechercher_selection = StringVar()    
b = -1
for r in range(3):
   for c in range(2):
        b = b+1
        radiobtn =Radiobutton(label_frame2,text=radio_taille_rechercher[b][0],value=radio_taille_rechercher[b][1], variable=taille_rechercher_selection,font=('Helvetica 10'))
        radiobtn.grid(row=5+r,column=c,sticky='W')

#Couleur de Cheveux
label_cheveux_rechercher=Label(label_frame2,text="Couleur de cheveux: ",font=('Helvetica 12'))
label_cheveux_rechercher.grid(row=8,column=0,sticky="W",)
liste_couleur_cheveux_rechercher =ttk.Combobox(label_frame2,values=["Noirs","Châtains","Blonds","Roux","Gris","Blanc"],state="readonly",width=22)
liste_couleur_cheveux_rechercher.grid(row=8,column=1)

#Couleur de Yeux 
label_yeux_rechercher=Label(label_frame2,text="Couleur des yeux: ",font=('Helvetica 12'))
label_yeux_rechercher.grid(row=9,column=0,sticky="W")
liste_couleur_yeux_rechercher=ttk.Combobox(label_frame2,values=["Noirs","Marrons","Verts","Bleus","Gris"],state="readonly",width=22)
liste_couleur_yeux_rechercher.grid(row=9,column=1,)

#Questionnaire 
label_consigne=Label(label_frame3,text="Pour finir, veuillez répondre à chacune des question en sachant que la note de 0 correspond à je déteste et la note 5 correspond à j'adore.",font=('Helvetica 11 italic')).pack()

#Question de 1 à 5
question_tuple= (('0', 0),('1', 1),('2', 2),('3', 3),('4', 4),('5', 5))
var_question1 =StringVar()
var_question2 = StringVar()
var_question3 = StringVar()
var_question4 = StringVar()
var_question5 =StringVar()
var_question6 =StringVar()
var_question7 =StringVar()
var_question8 =StringVar()
var_question9 =StringVar()
var_question10 = StringVar()    

#Boite contenant les questions 1 à 5 inclus
frame444=Frame(label_frame3)
frame444.pack(side=LEFT,pady=5)
#Boite Contenant les questions 6 à 10 inclus
frame445=Frame(label_frame3,)
frame445.pack(side=RIGHT)
#Question 1
label_question1=Label(frame444,text="Aimez-vous les animaux ?",font=('Helvetica 10')).grid(row=0,column=0,sticky="W")
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame444,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question1,font=('Helvetica 10'))
        radiobtn.grid(row=1,column=r,sticky='E')

#Question 2 
label_question2=Label(frame444,text="Aimez-vous voyager ?",font=('Helvetica 10')).grid(row=2,column=0,sticky="W")
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame444,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question2,font=('Helvetica 10'))
        radiobtn.grid(row=3,column=r,sticky='E')

#Question 3
label_question3=Label(frame444,text="Aimez-vous cuisiner ?",font=('Helvetica 10')).grid(row=4,column=0,sticky="W")
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame444,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question3,font=('Helvetica 10'))
        radiobtn.grid(row=5,column=r,sticky='E')

#Question 4
label_question4=Label(frame444,text="Aimez-vous les enfants ?",font=('Helvetica 10')).grid(row=6,column=0)
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame444,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question4,font=('Helvetica 10'))
        radiobtn.grid(row=7,column=r,sticky='E')

#Question 5 
label_question5=Label(frame444,text="Aimez-vous le cinéma ?",font=('Helvetica 10')).grid(row=8,column=0,sticky="W")
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame444,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question5,font=('Helvetica 10'))
        radiobtn.grid(row=9,column=r,sticky='E')

#Question 6
label_question6=Label(frame445,text="Aimez-vous le sport ?",font=('Helvetica 10')).grid(row=0,column=0,sticky="W")
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame445,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question6,font=('Helvetica 10'))
        radiobtn.grid(row=1,column=r,sticky='E')

#Question 7
label_question7=Label(frame445,text="Êtes-vous Romantique ?",font=('Helvetica 10')).grid(row=2,column=0,sticky="W")
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame445,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question7,font=('Helvetica 10'))
        radiobtn.grid(row=3,column=r,sticky='E')

#Question 8 
label_question8=Label(frame445,text="Êtes-vous proches de votre famille ?",font=('Helvetica 10')).grid(row=4,column=0,sticky="W")
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame445,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question8,font=('Helvetica 10'))
        radiobtn.grid(row=5,column=r,sticky='E')

#Question 9
label_question9=Label(frame445,text="Êtes-vous favorable au mariage ?",font=('Helvetica 10')).grid(row=6,column=0,sticky="W")
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame445,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question9,font=('Helvetica 10'))
        radiobtn.grid(row=7,column=r,sticky='E')

#Question 10
label_question10=Label(frame445,text="Aimez-vous sortir en boîte de nuit ?",font=('Helvetica 10')).grid(row=8,column=0,sticky="W")
b = -1
for r in range(6):
        b = b+1
        radiobtn =Radiobutton(frame445,text=question_tuple[b][0],value=question_tuple[b][1], variable=var_question10,font=('Helvetica 10'))
        radiobtn.grid(row=9,column=r,sticky='E')

#Texte description : 
texte_description=Text(label_frame4,width=60,height=10,font=('Helvetica 13'))
texte_description.pack(padx=5,pady=5)

#Bouton import photo de profile
import_btn=Button(label_frame5,text="Importer votre photo de profile",command= lambda:upload_file()).grid(row=0,column=0,padx=5,pady=1,sticky='NESW')

#Fonction pour rechercher et afficher une photo de profile

def upload_file():
    global img
    global filename
    f_types = [('Jpg Files', '*.jpg'),('PNG Files','*.png'),('All Files','*')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    width, height = img.size  
    width_new=int(width/3)
    height_new=int(height/3)
    img_resized=img.resize((width_new,height_new))
    img=ImageTk.PhotoImage(img_resized)
    b2 =tk.Label(label_frame5,image=img) # using Button 
    b2.grid(row=1,column=0)


boutton_envoyer=Button(page_inscription,text="S'inscrire",font=("Helvetica 15"),command=creation_compte)
boutton_envoyer.pack(side=LEFT,pady=7)

boutton_envoyer2=Button(page_inscription,text="Affichage",state="disabled",font=("Helvetica 15"),command=lambda:[show_frame(page_main),affichage()])
boutton_envoyer2.pack(side=LEFT,pady=7)


#Main menu,affichage,suppression
frame46 = Frame(page_main)
frame46.pack()

def affichage():
        global affichage_apercu
        affichage_apercu = []
        data_base_utilisateur_vers_data_base_convertie()
        for p_info in data_base_convertie:
                affichage_apercu.append([data_base_convertie[p_info]["Pseudo"],data_base_convertie[p_info]["Date_de_Naissance"],data_base_convertie[p_info]["Sexe"]])
        Update(affichage_apercu)

def Scankey(event):
    val = entry.get()
    if val == "":
        data = affichage_apercu
    else : 
        data= []
        for item in range(len(affichage_apercu)):
            if val.lower() in affichage_apercu[item][0].lower():
                data.append([affichage_apercu[item][0],affichage_apercu[item][1],affichage_apercu[item][2]])
    Update(data)


def Update(data):
        my_listbox.delete(0, 'end')
	# put new data
        for item in range(len(data)):
	        my_listbox.insert('end', data[item][0]+", "+data[item][1]+" ans, Genre : "+data[item][2])

label_seach = Label(frame46,text="Rechercher : ",font=('Helvetica 20'))
label_seach.grid(row=0,column=0)
entry = Entry(frame46,font=('Helvetica 18'))
entry.grid(row=0,column=1)

def supressions():
        name=(my_listbox.get(ANCHOR).split(","))
        supprimer(name[0])
        affichage()

def select():
        top = Toplevel()
        top.geometry("600x400")
        frame111 = Frame(top)
        
        frame111.pack(side=LEFT,fill="x")
        name=(my_listbox.get(ANCHOR).split(","))
       
        for i in data_base_convertie:
                if name[0]==data_base_convertie[i]["Pseudo"]:
                        label = Label(frame111,text="Prénom : "+str(data_base_convertie[i]["Pseudo"]))
                        label.grid(row=0,column=0,sticky='W')
                        label2= Label(frame111,text="Age : "+str(data_base_convertie[i]["Date_de_Naissance"]))
                        label2.grid(row=1,column=0,sticky='W')
                        label2= Label(frame111, text="Gender : "+str(data_base_convertie[i]["Sexe"]))
                        label2.grid(row=2,column=0,sticky='W')
                        label3=Label(frame111,text="Signe Astrologique : "+str(data_base_convertie[i]["Signe_Astrologie"]))
                        label3.grid(row=3,column=0,sticky="W")
                        label4=Label(frame111,text="Taille : "+str(data_base_convertie[i]["Taille"]))
                        label4.grid(row=4,column=0,sticky="W")
                        label5 =Label(frame111,text="Couleur de yeux : "+str(data_base_convertie[i]["Couleur_yeux"]))
                        label5.grid(row=5,column=0,sticky="W")
                        label6=Label(frame111,text="Couleur de chyeveux : "+str(data_base_convertie[i]["Couleur_cheveux"]))
                        label6.grid(row=6,column=0,sticky="W")
                        label7=Label(frame111,text="Recherche quelqu'un du sexe : "+str(data_base_convertie[i]["Sexe_rechercher"]))
                        label7.grid(row=8,column=0,sticky="W")
                        label8=Label(frame111,text="Age recherché : "+str(data_base_convertie[i]["Age_rechercher"]))
                        label8.grid(row=9,column=0,sticky="W")
                        label9=Label(frame111,text="Taille recherché : "+str(data_base_convertie[i]["Taille_rechercher"]))
                        label9.grid(row=10,column=0,sticky="W")
                        label10=Label(frame111,text="Couleur de cheveux recherché : "+str(data_base_convertie[i]["Cheveux_rechercher"]))
                        label10.grid(row=11,column=0,sticky="W")
                        label11=Label(frame111,text="Couleur de yeux : "+str(data_base_convertie[i]["Yeux_rechercher"]))
                        label11.grid(row=12,column=0,sticky="W")
                        label13=Label(frame111,text="Ayant répondu au questionnaire par :"+str(data_base_convertie[i]["Questionnaire"]))
                        label13.grid(row=13,column=0,sticky="W")
                        label12=Text(frame111,width=60,height=5,padx=5,font=('Helvetica'))
                        label12.grid(row=14,column=0,sticky="W")
                        label12.insert(1.0,"Bio : "+str(data_base_convertie[i]["Bio"]))
                        label12.configure(state='disabled')
                        img=Image.open(data_base_convertie[i]["Photo_Profile"])
                        width, height = img.size  
                        width_new=int(width/3)
                        height_new=int(height/3)
                        img_resized=img.resize((width_new,height_new))
                        img=ImageTk.PhotoImage(img_resized)
                        b2 =Label(frame111,image=img) 
                        b2.place(x=320,y=5)

        top.mainloop()

def scan(pseudo):
    fichier_vers_dico()
    for i in data_base_utilisateur:
        if data_base_utilisateur[i]['Pseudo'] == pseudo.upper() :
            return True
    else :
        return False
        
def compatibilite_deux():
        data_base_utilisateur_vers_data_base_convertie()
        def comparaison_deux():             
                if scan(entry_nom_personne1.get().upper()):
                        if scan(entry_nom_personne2.get().upper()):
                                label_resultat_comparaison.configure(text=compatibilite_entre_deux_personne(entry_nom_personne1.get().upper(),entry_nom_personne2.get().upper()))
                else:  messagebox.showwarning("Erreur compatibilité", "Erreur vérifier les personnes que vous souhaitez comparer")

        top = Toplevel()
        top.geometry("600x400")

        label_nom_personne1=Label(top,text="Entrer le nom de la première personne")
        label_nom_personne1.grid(row=0,column=0)
        entry_nom_personne1=Entry(top)
        entry_nom_personne1.grid(row=0,column=1)

        label_nom_personne2=Label(top,text="Entrer le nom de la deuxième personne")
        label_nom_personne2.grid(row=1,column=0)
        entry_nom_personne2=Entry(top)
        entry_nom_personne2.grid(row=1,column=1)
        
        comparaison_button=Button(top,text="Comparer",command=comparaison_deux)
        comparaison_button.grid(row=2,columnspan=2)
        
        label_resultat_comparaison=Label(top,text="")
        label_resultat_comparaison.grid(row=3)

        top.mainloop()


# compatibilite_deux()
def compatibilite_seul():
        data_base_utilisateur_vers_data_base_convertie()
        def comparaison_seul():             
                if scan(entry_nom_personne1.get().upper()):
                        position =0
                        list_trie_par_ordre_decroissant = compatibilite_personne1_vers_tous(entry_nom_personne1.get().upper())
                        if len(list_trie_par_ordre_decroissant)>5:
                                for i in list_trie_par_ordre_decroissant :
                                        if position ==5:
                                                break
                                        else :  
                                                label_resultat_comparaison2=Label(top,text="")
                                                label_resultat_comparaison2.grid(row=position+3)
                                                label_resultat_comparaison2.configure(text="N°"+str(position+1)+" "+str(i[0])+" avec : "+str(i[1])+"%")
                                                position += 1
                        else : 
                                for i in list_trie_par_ordre_decroissant :
                                        label_resultat_comparaison2=Label(top,text="")
                                        label_resultat_comparaison2.grid(row=position+3)
                                        label_resultat_comparaison2.configure(text="N°"+str(position+1)+" "+str(i[0])+" avec : "+str(i[1])+"%")
                                        position+=1
                        
        #                 label_resultat_comparaison.configure(text=compatibilite_entre_deux_personne(entry_nom_personne1.get())
                else:  messagebox.showwarning("Erreur compatibilité", "Erreur vérifier la personnes que vous souhaitez comparer")

        top = Toplevel()
        top.geometry("600x400")

        label_nom_personne1=Label(top,text="Entrer le nom de la personne")
        label_nom_personne1.grid(row=0,column=0)
        entry_nom_personne1=Entry(top)
        entry_nom_personne1.grid(row=0,column=1)

        
        comparaison_button=Button(top,text="Comparer",command=comparaison_seul)
        comparaison_button.grid(row=2,columnspan=2)

        label_resultat_comparaison2=Label(top,text="")
        label_resultat_comparaison2.grid(row=3,columnspan=2)

        top.mainloop()


my_listbox =Listbox(page_main,width=50,font=('Helvetica 18'))
my_listbox.pack(side = LEFT, fill = BOTH)

scrollbar = Scrollbar(page_main)
scrollbar.pack(side = RIGHT, fill = BOTH)
my_listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = my_listbox.yview)
my_button2 = Button(frame46,text="Afficher",command=select,font=('Helvetica 15'))
my_button2.grid(row=2,column=0)
my_button45 = Button(frame46,text="Supprimer",command=supressions,font=('Helvetica 15'))
my_button45.grid(row=2,column=1)
my_button558=Button(frame46,text="Compatibilité à deux",command=compatibilite_deux,font=('Helvetica 15'))
my_button558.grid(row=2,column=2)
my_button559=Button(frame46,text="Compatibilité seul",command=compatibilite_seul,font=('Helvetica 15'))
my_button559.grid(row=2,column=3)
my_button3 = Button(frame46,text="Inscription",command=lambda:show_frame(page_inscription),font=('Helvetica 15'))
my_button3.grid(row=2,column=4)
entry.bind('<KeyRelease>', Scankey)


show_frame(page_accueil)#On lance l'affichage graphique sur avec la page accueil
page_accueil.after(4000, changement_titre_devise)
root.mainloop()#On lance l'application



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

