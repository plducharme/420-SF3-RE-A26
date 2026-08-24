from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QMessageBox, QWidget
from PySide6.QtCore import QTranslator, QLocale, QLibraryInfo


class QMessageBoxEx(QMainWindow):
    def __init__(self):
        super().__init__()

        self.traduire_francais()

        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        self.setWindowTitle("Exemples QMessageBox")
        disposition = QGridLayout()
        widget_central.setLayout(disposition)

        bouton_a_propos = QPushButton("À propos")
        # Fonction statique qui génère une fenêtre "About"
        bouton_a_propos.clicked.connect(lambda: QMessageBox.about(self, "À Propos", "Copyright 2023"))
        disposition.addWidget(bouton_a_propos, 0, 0)

        bouton_critique = QPushButton("Critique")
        bouton_critique.clicked.connect(lambda: QMessageBox.critical(self, "Erreur Critique", "Une erreur critique est "
                                                                                              "survenue"))
        disposition.addWidget(bouton_critique, 1, 0)

        bouton_information = QPushButton("Information")
        bouton_information.clicked.connect(lambda: QMessageBox.information(self, "Information", "Information à "
                                                                                                "afficher"))
        disposition.addWidget(bouton_information, 2, 0)

        bouton_avertissement = QPushButton("Avertissement")
        bouton_avertissement.clicked.connect(lambda: QMessageBox.warning(self, "Avertissement", "Avertissement: qqc "
                                                                                                "s'est produit"))
        disposition.addWidget(bouton_avertissement, 3, 0)

        bouton_question = QPushButton("Question")
        bouton_question.clicked.connect(self.bouton_question_clicked)
        disposition.addWidget(bouton_question, 0, 1)

        bouton_personnalise = QPushButton("Bouton personnalisé")
        bouton_personnalise.clicked.connect(self.bouton_personnalise_clicked)
        disposition.addWidget(bouton_personnalise, 1, 1)

    def bouton_question_clicked(self):
        bouton_clicked = QMessageBox.question(self, "Questions", "Vraiment?", QMessageBox.StandardButton.Yes |
                                              QMessageBox.StandardButton.No)
        if bouton_clicked == QMessageBox.StandardButton.Yes:
            print("Réponse Question: Oui")
        elif bouton_clicked == QMessageBox.StandardButton.No:
            print("Réponse Question: Non")

    def bouton_personnalise_clicked(self):
        message_box = QMessageBox(self)
        message_box.setText("QMessageBox personnalisé avec un choix de boutons pour la sauvegarde")
        message_box.setInformativeText("Voulez vous enregistrer les modifications?")
        message_box.setStandardButtons(QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard |
                                       QMessageBox.StandardButton.Cancel)
        message_box.setDefaultButton(QMessageBox.StandardButton.Save)
        message_box.setDetailedText("Texte détaillé sur ce qui est arrivé")
        bouton_clicked = message_box.exec()

        if bouton_clicked == QMessageBox.StandardButton.Save:
            print("Code pour la sauvegarde")
        elif bouton_clicked == QMessageBox.StandardButton.Discard:
            print("Code pour le rejet des changements")
        elif bouton_clicked == QMessageBox.StandardButton.Cancel:
            print("Annuler")

    # Pour utliser les traductions françaises pour les widgets
    def traduire_francais(self):
        # Initialise le traducteur
        traducteur = QTranslator(self)
        # Charge le fichier provenant de Pyside6 contenant les traductions
        # Contenu dan Pyside6/translations/qt_<code de langue>.qm
        traducteur.load("qt_fr.qm", QLibraryInfo.path(QLibraryInfo.TranslationsPath))
        # On va chercher l'instance de l'application en cours pour installer le traducteur
        QApplication.instance().installTranslator(traducteur)


app = QApplication()
qmb = QMessageBoxEx()
qmb.show()
app.exec()
