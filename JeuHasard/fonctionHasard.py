from tkinter import messagebox

def description():
    messagebox.showinfo("À propos","Nom jeu: Chiffre Exact\nCréateur: Ariste kindy\nDate de création: 16 novembre 2022\nVersion: 10.0.0.1")

def reglement():
    message = "Chiffre exact est un jeu, dans lequel vous commencez "
    message += "avec un score de 50 points. un chiffre est déjà choisit "
    message += "pour vous le but c'est de trouver le chiffre déjà choisit "
    message += "par vous même. À chaque mauvais chiffre choisit, votre score "
    message += "baisse de 5 points et le programme va vous indiquer si c'est "
    message += "supérieur ou non. Si vous trouvez le chiffre exact avant que votre "
    message += "score est à zéro,vous avez gagné sinon vous perdez."
    messagebox.showinfo("Règlemnent", message)

def sauvegarder(x):
    file = open("C:\\Users\\arist\\JeuHasard\\Hasard.txt", "w") 
    file.write(x)
    file.close()

def historique():
    fic = open("C:\\Users\\arist\\JeuHasard\\Hasard.txt", "r")
    z = fic.read()
    messagebox.showinfo("Historique", z)


