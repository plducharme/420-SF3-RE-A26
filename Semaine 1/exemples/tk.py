from tkinter import Tk, Button, Label


class Window(Tk):

    def __init__(self):
        super().__init__()
        # Titre de la fenetre
        self.title("Test de Tk")
        # Ajout d'un texte
        self.label = Label(text="Cliquez pour fermer")
        self.label.pack()
        # Ajout d'un bouton
        self.button = Button(text="Fermer", command=self.handle_button_press)
        self.button.pack()

    # Gestion de l'evenement du bouton
    def handle_button_press(self):
        self.destroy()


# Creation de la fenetre
window = Window()
# Boucle principale
window.mainloop()
