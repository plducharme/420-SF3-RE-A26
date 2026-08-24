from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QApplication, QTextEdit, QComboBox, QVBoxLayout, \
    QHBoxLayout, QLabel
from enum import Enum
from client_hugging_face import HuggingFaceClient, Fournisseur


class ApplicationAI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.client_hugging_face = HuggingFaceClient()
        self.setWindowTitle("Application AI")
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.disposition_principale = QVBoxLayout()
        self.main_widget.setLayout(self.disposition_principale)
        self.disposition_type_requete = QHBoxLayout()
        self.disposition_type_requete.addWidget(QLabel("Type de requête : "))

        self.combobox_fournisseurs = QComboBox()
        self.combobox_type_requete = QComboBox()
        self.combobox_type_requete.currentIndexChanged.connect(self.combobox_type_requete_changed)
        self.disposition_type_requete.addWidget(self.combobox_type_requete)
        for type_requete in TypeRequete:
            self.combobox_type_requete.addItem(type_requete.value)


        # self.get_fournisseurs_type_requete()
        self.disposition_fournisseurs = QHBoxLayout()
        self.disposition_fournisseurs.addWidget(QLabel("Fournisseur : "))
        self.disposition_fournisseurs.addWidget(self.combobox_fournisseurs)

        self.disposition_principale.addLayout(self.disposition_type_requete)
        self.disposition_principale.addLayout(self.disposition_fournisseurs)

        self.prompt = QTextEdit()
        self.disposition_principale.addWidget(self.prompt)
        self.bouton = QPushButton("Envoyer")
        self.bouton.clicked.connect(self.bouton_clicked)
        self.disposition_principale.addWidget(self.bouton)

    def combobox_type_requete_changed(self, index):
        self.get_fournisseurs_type_requete()


    def bouton_clicked(self):
        type_requete = self.combobox_type_requete.currentText()
        if type_requete == TypeRequete.CHAT.value:
            reponse = self.client_hugging_face.executer_requete_chat(texte_input=self.prompt.toPlainText(),
                                                                     modele=self.combobox_fournisseurs.currentData()[1],
                                                                     fournisseur=self.combobox_fournisseurs.currentData()[0])
        elif type_requete == TypeRequete.IMAGE.value:
            reponse = self.client_hugging_face.generer_image_pil(self.combobox_fournisseurs.currentData()[1],
                                                             self.prompt.toPlainText(),
                                                             fournissseur=self.combobox_fournisseurs.currentData()[0])
            reponse.show()
        else:
            reponse = "Type de requête non reconnu"

        print(reponse)

    def get_fournisseurs_type_requete(self):
        type_requete = self.combobox_type_requete.currentText()
        liste_fournisseurs_modeles = []
        if type_requete == TypeRequete.CHAT.value:
            liste_fournisseurs_modeles = [(Fournisseur.FIREWORKS, "deepseek-ai/DeepSeek-V3-0324"),
                                          (Fournisseur.CEREBRAS, "meta-llama/Llama-3.3-70B-Instruct")]
        elif type_requete == TypeRequete.IMAGE.value:
            liste_fournisseurs_modeles = [(Fournisseur.FAL_AI, "black-forest-labs/FLUX.1-dev")]
        self.combobox_fournisseurs.clear()
        for fournisseur in liste_fournisseurs_modeles:
            self.combobox_fournisseurs.addItem(fournisseur[0].value, userData=fournisseur)



class TypeRequete(Enum):
    CHAT = "Discuter"
    IMAGE = "Générer une image"


if __name__ == "__main__":
    app = QApplication([])
    window = ApplicationAI()
    window.show()
    app.exec()
