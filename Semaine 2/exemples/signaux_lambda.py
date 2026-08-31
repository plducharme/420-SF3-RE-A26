from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel


class SignauxLambda(QWidget):
    def __init__(self):
        # On créé une fenêtre à partir d'un widget générique
        super().__init__()
        disposition = QVBoxLayout()
        self.setLayout(disposition)
        self.libelle_msg = QLabel("Message par défaut")
        disposition.addWidget(self.libelle_msg)

        # Bouton avec signal connecté à une méthode
        bouton_methode = QPushButton("Bouton connecté à une méthode")
        # façon usuelle, on le connecte à une méthode en passant la référence vers la méthode
        bouton_methode.clicked.connect(self.bouton_methode_clicked)
        disposition.addWidget(bouton_methode)

        # Bouton utilisant un lambda à la place
        bouton_lambda = QPushButton("Bouton utilisant un lambda")
        # Au lieu de connecter à une méthode, on définit un lambda qui retourne une fonction anonyme.
        # Comme l'appel de la méthode fait partie de la définition du lambda, l'appel se fera seulement lorsque le
        # lambda sera appelé. Pratique pour faire un appel simple contenant des arguments sans avoir à connecter une
        # méthode ne contenant qu'une ligne...
        bouton_lambda.clicked.connect(lambda x: self.libelle_msg.setText("lambda appelé"))
        disposition.addWidget(bouton_lambda)

    def bouton_methode_clicked(self):
        self.libelle_msg.setText("Bouton méthode cliqué")


app = QApplication()
sl = SignauxLambda()
sl.show()
app.exec()
