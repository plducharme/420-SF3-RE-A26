from tkinter import Tk, Button, Label
from random import choice


class Window(Tk):

    def __init__(self):
        super().__init__()
        self.citations = []
        self.read_citations()

        # Titre de la fenetre
        self.title("Sagesse")
        # Ajout d'un texte
        self.label = Label(text=self.format_citation(choice(self.citations)))
        self.label.pack()
        # Ajout d'un bouton
        self.button = Button(text="Fermer", command=self.handle_button_press)
        self.button.pack()

    # Gestion de l'evenement du bouton
    def handle_button_press(self):
        self.destroy()

    # Lecture du fichier et ajout des citations à une liste
    def read_citations(self):
        with open('citations.txt', 'r', encoding="utf-8") as reader:
            for ligne in reader:
                self.citations.append(ligne)

    # Formatage de la citation selon les directives
    def format_citation(self, citation):
        split_str = citation.split()
        resultat = ""
        i = 1
        for mot in split_str:
            # Cas du \n devant l'auteur
            if mot.startswith("-"):
                resultat += "\n" + mot
            else:
                resultat += mot
                # Ajout de \n à chaque 3 mots
                if i % 3 == 0:
                    resultat += "\n"
            resultat += " "
            i = i+1
        return resultat


# Creation de la fenêtre
window = Window()
# Boucle principale
window.mainloop()