from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QButtonGroup, QHBoxLayout
from PySide6.QtGui import QIcon


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        radio_canard = QRadioButton("Canard")
        radio_canard.setIcon(QIcon('canard.png'))
        radio_orni = QRadioButton("Ornithorynque")
        radio_chien = QRadioButton("Chien")
        radio_orni.setChecked(True)

        groupe_boutons = QButtonGroup()
        groupe_boutons.addButton(radio_canard)
        groupe_boutons.addButton(radio_orni)
        groupe_boutons.addButton(radio_chien)

        widget_group = QWidget()
        disposition_bouton_group = QHBoxLayout()
        widget_group.setLayout(disposition_bouton_group)

        disposition_bouton_group.addWidget(radio_canard)
        disposition_bouton_group.addWidget(radio_orni)
        disposition_bouton_group.addWidget(radio_chien)
        disposition.addWidget(widget_group)

        radio_furet = QRadioButton("Furet")
        radio_souris = QRadioButton("Souris")
        radio_rat = QRadioButton("Rat")

        groupe_boutons_rongeurs = QButtonGroup()
        groupe_boutons_rongeurs.addButton(radio_furet)
        groupe_boutons_rongeurs.addButton(radio_souris)
        groupe_boutons_rongeurs.addButton(radio_rat)

        widget_group_rongeurs = QWidget()
        disposition_bouton_group_rongeurs = QHBoxLayout()
        disposition_bouton_group_rongeurs.addWidget(radio_furet)
        disposition_bouton_group_rongeurs.addWidget(radio_souris)
        disposition_bouton_group_rongeurs.addWidget(radio_rat)
        widget_group_rongeurs.setLayout(disposition_bouton_group_rongeurs)
        disposition.addWidget(widget_group_rongeurs)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()