from PySide6.QtWidgets import (QApplication, QMessageBox, QMainWindow, QLabel, QFileDialog, QFrame, QMenu, QGridLayout,
                               QLineEdit, QHBoxLayout, QPushButton)
from PySide6.QtGui import QAction
import logging
import pandas as pd
from pandas import DataFrame

logger = logging.getLogger(__name__)


class AnalyseurDeDonnees(QMainWindow):

    def __init__(self):
        super().__init__()

        # configuration du logger
        # il est possible d'envoyer les logs dans un fichier, à la console, dans un système de messagerie, etc
        # Le niveau de logging permet de filtrer pour obtenir seulement les logs à un certain niveau et ceux plus élevés
        # NOTSET -> DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL
        # format permet de spécifier sous quel format le message sera affiché
        logging.basicConfig(filename="analyseur.log",
                            level=logging.INFO,
                            format="%(levelname)s:%(name)s:%(message)s",
                            filemode="a",
                            encoding="utf8")
        logger.debug("Application démarrée")

        self.widget_principal = QFrame()
        self.setCentralWidget(self.widget_principal)
        self.disposition_principale = QGridLayout()
        self.widget_principal.setLayout(self.disposition_principale)
        self.setWindowTitle("Analyseur de collisions d'oiseaux")

        # menu
        self.barre_menu = self.menuBar()
        self.menu_fichier = QMenu("F&ichier")
        self.barre_menu.addMenu(self.menu_fichier)
        self.action_importer_donnees = QAction("Import du csv")
        self.action_importer_donnees.triggered.connect(self.import_donnees)
        self.action_importer_donnees.setShortcut("Ctrl+o")
        self.menu_fichier.addAction(self.action_importer_donnees)
        self.menu_fichier.addSeparator()
        self.action_quitter = QAction("Quitter")
        self.action_quitter.triggered.connect(self.close)
        self.menu_fichier.addAction(self.action_quitter)

        self.libelle_nb_enregistrements = QLabel("Nombre enregistrements:")
        self.disposition_principale.addWidget(self.libelle_nb_enregistrements, 1, 1)
        self.nb_enregistrements = QLabel("N/D")
        self.disposition_principale.addWidget(self.nb_enregistrements, 1, 2)
        self.libelle_moyenne_collisions = QLabel("Moyenne de collisions d'oiseaux dans l'intervalle [N/D, N/D]:")
        self.disposition_principale.addWidget(self.libelle_moyenne_collisions, 2, 1)
        self.moyenne_collisions = QLabel("N/D")
        self.disposition_principale.addWidget(self.moyenne_collisions, 2, 2)

        self.disposition_intervalle = QHBoxLayout()
        self.libelle_debut = QLabel("[")
        self.input_debut = QLineEdit()
        self.input_debut.setEnabled(False)
        self.input_debut.setMask("00000000")
        self.disposition_intervalle.addWidget(self.libelle_debut)
        self.disposition_intervalle.addWidget(self.input_debut)
        self.libelle_intervalle_virgule = QLabel(",")
        self.input_fin = QLineEdit()
        self.input_fin.setEnabled(False)
        self.setMask("00000000")
        self.disposition_intervalle.addWidget(self.input_fin)
        self.libelle_fin = QLabel("]")
        self.disposition_intervalle.addWidget(self.libelle_fin)
        self.bouton_calcul = QPushButton("Calcul")
        self.bouton_calcul.setEnabled(False)
        self.bouton_calcul.clicked.connect(self.calcul_moyenne_collisions)
        self.disposition_intervalle.addWidget(self.bouton_calcul)
        self.disposition_principale.addLayout(self.disposition_intervalle, 3, 1, 1, 2)
        self.libelle_message = QLabel()
        self.libelle_message.setStyleSheet("color: red")
        self.libelle_message.hide()
        self.disposition_principale.addWidget(self.libelle_message, 4, 1, 1, 2)

        self.df: DataFrame | None = None

    def import_donnees(self):
        fichier, filtres = QFileDialog.getOpenFileName(self, "Ouvrir un csv", ".", "*.csv")
        if fichier:
            try:
                self.df = pd.read_csv(fichier)
                self.input_debut.setText("0")
                self.input_debut.setEnabled(True)
                self.input_fin.setText(str(len(self.df) - 1))
                self.input_fin.setEnabled(True)
                self.bouton_calcul.setEnabled(True)
                self.nb_enregistrements.setText(str(len(self.df)))

            except Exception as e:
                logger.error(f"Mauvais format csv:\n {e}")
                QMessageBox.warning(self, "Erreur d'import csv",
                                    "Mauvais format csv!\nVeuillez charger un autre fichier.")

    def calcul_moyenne_collisions(self):
        self.libelle_message.setText("")
        self.libelle_message.hide()
        debut = int(self.input_debut.text())
        erreur = False
        # valider l'input
        if debut < 0:
            self.libelle_message.setText("L'index de début ne peut pas être négatif")
            erreur = True
        fin = int(self.input_fin.text())
        if fin > len(self.df) - 1:
            if len(self.libelle_message.text()) > 0:
                message = f"{self.libelle_message.text()}\nL'index de fin ne peut être supérieur à {len(self.df) - 1}"
            else:
                message = f"L'index de fin ne peut être supérieur à {len(self.df) - 1}"
            self.libelle_message.setText(message)
            erreur = True
        if erreur:
            self.libelle_message.show()
            return
        intervalle_df: DataFrame = self.df[debut:fin]
        try:
            moyenne = intervalle_df["NumberStruckActual"].mean()
            self.libelle_moyenne_collisions.setText(
                f"Moyenne de collisions d'oiseaux dans l'intervalle [{debut}, {fin}]:")
            self.moyenne_collisions.setText(f"{moyenne}")
        except Exception as e:
            logger.error(f"Erreur de calcul de moyenne\n{e}")
            QMessageBox.critical(self, "Erreur de calcul", "Erreur de calcul de moyenne, veuillez contacter le support")
            return


if __name__ == "__main__":
    app = QApplication()
    ad = AnalyseurDeDonnees()
    ad.show()
    app.exec()
