from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton, QApplication, QTextEdit, QComboBox, QVBoxLayout
from pipelines import ExemplesPipeline


class OutilsAILocal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Outils AI Local")
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.disposition_principale = QVBoxLayout()
        self.main_widget.setLayout(self.disposition_principale)

        self.type_requete = QComboBox()
        self.type_requete.addItem("Classification sentiment de texte", userData="classification_texte")
        self.type_requete.addItem("Génération d'image", userData="generation_image")
        self.disposition_principale.addWidget(self.type_requete)

        self.prompt = QTextEdit()
        self.disposition_principale.addWidget(self.prompt)
        self.bouton_envoyer = QPushButton("Envoyer")
        self.bouton_envoyer.clicked.connect(self.bouton_envoyer_clicked)
        self.disposition_principale.addWidget(self.bouton_envoyer)

        self.resultat = QTextEdit()
        self.resultat.setReadOnly(True)
        self.disposition_principale.addWidget(self.resultat)

    def bouton_envoyer_clicked(self):
        texte_input = self.prompt.toPlainText()
        match self.type_requete.currentData():
            case "classification_texte":
                resultat = ExemplesPipeline.classification_sentiment_texte(texte_input)
                self.resultat.append(f"Sentiment : {resultat}\n")
            case "generation_image":
                image_path = ExemplesPipeline.texte_vers_image(texte_input)
                self.resultat.append(f"Image générée : {image_path}\n")
            case _:
                self.resultat.append("Type de requête non reconnu")


if __name__ == "__main__":
    app = QApplication([])
    fenetre = OutilsAILocal()
    fenetre.show()
    app.exec()

