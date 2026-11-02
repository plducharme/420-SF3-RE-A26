from PySide6.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout, QTextEdit
from PySide6.QtCore import Qt, QEvent, QSize, QCoreApplication


class EvenementPersonnalise(QEvent):
    # variable de classe pour enregistrer l'événement personnalisé
    EventType = QEvent.Type(QEvent.registerEventType())

    def __init__(self, donnees: dict):
        super().__init__(EvenementPersonnalise.EventType)
        self.donnees = donnees


class Fenetre(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple d'événement personnalisé")

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.output = QTextEdit()
        self.disposition.addWidget(self.output)

        self.bouton_1 = QPushButton("Bouton 1")
        self.bouton_1.setObjectName("Super Duper Bouton 1")
        self.bouton_1.setMinimumSize(QSize(100, 50))
        self.bouton_1.clicked.connect(self.envoyer_evenement)
        self.disposition.addWidget(self.bouton_1)

        self.bouton_2 = QPushButton("Bouton 2")
        self.bouton_2.setObjectName("Mega Bouton 2")
        self.bouton_2.setMinimumSize(QSize(150, 75))
        self.bouton_2.clicked.connect(self.envoyer_evenement)
        self.disposition.addWidget(self.bouton_2)

    # Méthode pour générer et envoyer notre EvenementPersonnalise
    def envoyer_evenement(self):
        origine = self.sender()
        donnees = {
            "source": origine.objectName(),
            "grandeur": f"largeur: {origine.size().width()} hauteur: {origine.size().height()}"
        }

        evenement = EvenementPersonnalise(donnees)
        # On envoie l'événement via l'application. Le premier paramètre est le receveur de l'événement (ex: fenêtre, widget)
        # Le receveur doit redéfinir la méthode event() pour gérer l'événement, dans ce cas-ci, on le renvoie à la fenêtre courante
        # postEvent() envoie de façon asynchrone
        # sendEvent() envoie de façon synchrone
        QCoreApplication.postEvent(self, evenement)

    # Méthode redéfinie pour gérer les événements
    def event(self, event, /):

        if event.type() == EvenementPersonnalise.EventType:
            evenement: EvenementPersonnalise = event
            self.output.append(
                f"Expéditeur: {evenement.donnees["source"]}\tgrandeur: {evenement.donnees["grandeur"]}\n")
            return True
        else:
            # pour que les autres événements soient gérés normalement
            return super().event(event)


app = QApplication()
fenetre = Fenetre()
fenetre.show()
app.exec()
