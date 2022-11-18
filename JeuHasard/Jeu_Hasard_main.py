#Importation des librairies
import tkinter
import fonctionHasard
import random
from tkinter import messagebox

#Class
class JeuHasard:

    def __init__(self):
        self.listepartie = []
        self.score = int(50)
        self.tentative = int(0)
        self.nombreExact = random.randint(1, 100)

    def _setScore(self):
        self.score -= 5

    def _setTentative(self):
        self.tentative += 1

    def _getNombreExact(self):
        return self.nombreExact

    def _getTentative(self):
        return self.tentative

    def _getScore(self):
        return self.score

    def _addParti(self, partie):
        self.listepartie.append[partie]

    def _getParti(self):
        return self.listepartie

    def _getNombreExact(self):
        return self.nombreExact

    def _telecharger(self,x):
        fic = open(x, "r")
        z = fic.read()
        self.listepartie.append(z)

#Structure interface et code
jeu = tkinter.Tk()

jeu.tk.call(
  'wm', 
  'iconphoto', 
  jeu._w, 
  tkinter.PhotoImage(file="C:\\Users\\arist\\OneDrive\\Documents\\JeuHasard\\logo-chiffre-ecxat.png")
)

jeu.title("Chiffre excat")

ecran_x = int(jeu.winfo_screenwidth())
ecran_y = int(jeu.winfo_screenheight())
ecranApp_x = 475
ecranApp_y = 500
pos_x = (ecran_x // 2) - (ecranApp_x // 2)
pos_y = (ecran_y // 2) - (ecranApp_y // 2)
geo = "{}x{}+{}+{}".format(ecranApp_x,ecranApp_y,pos_x,pos_y)
jeu.geometry(geo)
jeu.minsize(ecranApp_x,ecranApp_y)
jeu.maxsize(ecranApp_x,ecranApp_y)

#Creation de la structure du jeu
jwet = JeuHasard()
jwet._telecharger("C:\\Users\\arist\\JeuHasard\\Hasard.txt")
#print(jwet._getNombreExact())
#fonction
def hasard():
    if (0 < numero.get() < 101):
        jwet._setTentative()
        if(numero.get() == jwet._getNombreExact()):
            message = jwet._getParti()[0]
            message += "\n(Vaincu) Tentative: {}, Score: {},Chiffre exact: {}".format(jwet._getTentative(),jwet._getScore(),jwet._getNombreExact())
            fonctionHasard.sauvegarder(message)
            imgWin = tkinter.Label(jeu, text=str("☺"), font=("MADEAvenuePERSONALUSE-Regular",250),fg="orange")
            imgWin.place(relx=0.50, rely=0.45,width=400,height=360, anchor= "center")
            gagne = tkinter.Label(jeu, text=str("Vous avez gagné"), font=("MADEAvenuePERSONALUSE-Regular",40), fg="orange")
            gagne.place(relx=0.50, rely=0.90, anchor= "center")
        if(numero.get() < jwet._getNombreExact()):
            jwet._setScore()
            nscore = tkinter.Label(jeu, text=str("   "), font=("MADEAvenuePERSONALUSE-Regular",15), fg="green")
            nscore.place(relx=0.95, rely=0.030, anchor= "center")
            nscore = tkinter.Label(jeu, text=str(jwet._getScore()), font=("MADEAvenuePERSONALUSE-Regular",15), fg="green")
            nscore.place(relx=0.95, rely=0.030, anchor= "center")
            texte2cisioni = tkinter.Label(jeu, text="                                                    \n                 ", font=("MADEAvenuePERSONALUSE-Regular",15), fg= "red")
            texte2cisioni.place(relx=0.50, rely=0.75, anchor= "center")
            texte2cisioni = tkinter.Label(jeu, text="Votre chiffre est inferieur\nau chiffre exact.", font=("MADEAvenuePERSONALUSE-Regular",15), fg= "red")
            texte2cisioni.place(relx=0.50, rely=0.75, anchor= "center")
        if(numero.get() > jwet._getNombreExact()):
            jwet._setScore()
            nscore = tkinter.Label(jeu, text=str("   "), font=("MADEAvenuePERSONALUSE-Regular",15), fg="green")
            nscore.place(relx=0.95, rely=0.030, anchor= "center")
            nscore = tkinter.Label(jeu, text=str(jwet._getScore()), font=("MADEAvenuePERSONALUSE-Regular",15), fg="green")
            nscore.place(relx=0.95, rely=0.030, anchor= "center")
            texte2cisions = tkinter.Label(jeu, text="                                                    \n                 ", font=("MADEAvenuePERSONALUSE-Regular",15), fg= "red")
            texte2cisions.place(relx=0.50, rely=0.75, anchor= "center")
            texte2cisions = tkinter.Label(jeu, text="Votre chiffre est supérieur\nau chiffre exact.", font=("MADEAvenuePERSONALUSE-Regular",15), fg= "red")
            texte2cisions.place(relx=0.50, rely=0.75, anchor= "center")
        if(jwet._getScore() == int(0)):
            message = jwet._getParti()[0]
            message += "\n(Perdu ) Tentative: {}, Score: {},Chiffre exact: {}".format(jwet._getTentative(),jwet._getScore(),jwet._getNombreExact())
            fonctionHasard.sauvegarder(message)
            nscore = tkinter.Label(jeu, text=str("   "), font=("MADEAvenuePERSONALUSE-Regular",15), fg="green")
            nscore.place(relx=0.95, rely=0.030, anchor= "center")
            nscore = tkinter.Label(jeu, text=str(jwet._getScore()), font=("MADEAvenuePERSONALUSE-Regular",15), fg="green")
            nscore.place(relx=0.95, rely=0.030, anchor= "center")
            perdre = tkinter.Label(jeu, text=str("Vous avez\nperdu!"), font=("MADEAvenuePERSONALUSE-Regular",40), fg="red")
            perdre.place(relx=0.50, rely=0.45,width=400,height=360, anchor= "center")
    else:
        texte2cisions = tkinter.Label(jeu, text="                                                       \n                 ", font=("MADEAvenuePERSONALUSE-Regular",15), fg= "red")
        texte2cisions.place(relx=0.50, rely=0.75, anchor= "center")
        texte2cisions = tkinter.Label(jeu, text="Votre chiffre n'est pas compris\nentre 0 et 101 !", font=("MADEAvenuePERSONALUSE-Regular",15), fg= "red")
        texte2cisions.place(relx=0.50, rely=0.75, anchor= "center")

#Création menu
menu_jeu = tkinter.Menu(jeu)

historique_jeu = tkinter.Menubutton(jeu)

reglement_jeu = tkinter.Menubutton(jeu)

aPropos_jeu = tkinter.Menubutton(jeu)

menu_jeu.add_cascade(label="Historique", menu=historique_jeu,command=fonctionHasard.historique)

menu_jeu.add_cascade(label="Règlement", menu=reglement_jeu,command=fonctionHasard.reglement)

menu_jeu.add_cascade(label="Àpropos", menu=aPropos_jeu,command=fonctionHasard.description)

#ajout texte,entry et bouton
bienvenue = tkinter.Label(jeu, text = "Bienvenue", font =("barefood sign", 70), fg = "orange")
sur = tkinter.Label(jeu, text = "Sur", font =("barefood sign", 33), fg = "orange")
chiffreEcxat = tkinter.Label(jeu, text = "Chiffre exact", font = ("food secret", 30), fg = "orange")


sur.place(relx = 0.50, rely = 0.29, anchor = "center")
bienvenue.place(relx = 0.50, rely = 0.19, anchor = "center")
chiffreEcxat.place(relx = 0.50, rely = 0.37, anchor = "center")

texte1 = tkinter.Label(jeu, text="Entrez un chiffre compris entre 0 et 101 :", font=("MADEAvenuePERSONALUSE-Regular",15))
texte1.place(relx=0.50, rely=0.45, anchor= "center")

numero = tkinter.IntVar()
entree1 = tkinter.Entry(jeu,textvariable=numero,font=("Calibri",30))


entree1.place(relx = 0.50, rely = 0.53,width=280,height=45,anchor = "center")

bouton3 = tkinter.Button(jeu, text = "Vérifier", font = ("MADEAvenuePERSONALUSE-Regular", 15), fg = "black", bg = "azure",command=hasard)
bouton3.place(relx = 0.50, rely = 0.63, anchor = "center")


score = tkinter.Label(jeu, text="Score:", font=("MADEAvenuePERSONALUSE-Regular",15), fg="green")
score.place(relx=0.87, rely=0.030, anchor= "center")

nscore = tkinter.Label(jeu, text=str("50"), font=("MADEAvenuePERSONALUSE-Regular",15), fg="green")
nscore.place(relx=0.95, rely=0.030, anchor= "center")

#Boucle principale
jeu.config(menu=menu_jeu)
jeu.mainloop()
