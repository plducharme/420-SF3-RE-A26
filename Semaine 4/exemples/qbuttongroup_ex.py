from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QFrame, QRadioButton, QButtonGroup, QCheckBox, \
    QGroupBox


class GroupeBoutonEx(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de groupes de boutons")

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        diete_bouton_radio_omnivore = QRadioButton("Omnivore")
        diete_bouton_radio_omnivore.setChecked(True)
        diete_bouton_radio_vegetarien = QRadioButton("Végétarien")
        diete_bouton_radio_vegetalien = QRadioButton("Végan")
        self.bouton_groupe_diete = QButtonGroup()
        self.bouton_groupe_diete.addButton(diete_bouton_radio_omnivore)
        self.bouton_groupe_diete.addButton(diete_bouton_radio_vegetarien)
        self.bouton_groupe_diete.addButton(diete_bouton_radio_vegetalien)

        disposition_boutons_diete = QHBoxLayout()
        disposition_boutons_diete.addWidget(diete_bouton_radio_omnivore)
        disposition_boutons_diete.addWidget(diete_bouton_radio_vegetarien)
        disposition_boutons_diete.addWidget(diete_bouton_radio_vegetalien)

        self.bouton_radio_independant_1 = QRadioButton("Indépendant 1")
        self.bouton_radio_independant_2 = QRadioButton("Indépendant 2")
        self.bouton_radio_independant_3 = QRadioButton("Indépendant 3")

        self.groupe_boutons_radio_independant = QButtonGroup()
        self.groupe_boutons_radio_independant.addButton(self.bouton_radio_independant_1)
        self.groupe_boutons_radio_independant.addButton(self.bouton_radio_independant_2)
        self.groupe_boutons_radio_independant.addButton(self.bouton_radio_independant_3)
        self.groupe_boutons_radio_independant.setExclusive(False)

        disposition_boutons_independants = QHBoxLayout()
        disposition_boutons_independants.addWidget(self.bouton_radio_independant_1)
        disposition_boutons_independants.addWidget(self.bouton_radio_independant_2)
        disposition_boutons_independants.addWidget(self.bouton_radio_independant_3)

        disposition.addLayout(disposition_boutons_independants)
        disposition.addLayout(disposition_boutons_diete)

        groupe_options_1 = QGroupBox()
        groupe_options_1.setCheckable(True)
        self.groupe_options_cases_a = QCheckBox("A")
        self.groupe_options_cases_b = QCheckBox("B")
        self.groupe_options_cases_c = QCheckBox("C")
        disposition_options_1 = QVBoxLayout()
        disposition_options_1.addWidget(self.groupe_options_cases_a)
        disposition_options_1.addWidget(self.groupe_options_cases_b)
        disposition_options_1.addWidget(self.groupe_options_cases_c)
        groupe_options_1.setLayout(disposition_options_1)
        disposition.addWidget(groupe_options_1)

        groupe_options_2 = QGroupBox()
        groupe_options_2.setCheckable(True)
        self.option_radio_1 = QRadioButton("Option 1")
        self.option_radio_2 = QRadioButton("Option 2")
        self.option_radio_3 = QRadioButton("Option 3")
        disposition_options_2 = QVBoxLayout()
        disposition_options_2.addWidget(self.option_radio_1)
        disposition_options_2.addWidget(self.option_radio_2)
        disposition_options_2.addWidget(self.option_radio_3)
        groupe_options_2.setLayout(disposition_options_2)
        groupe_options_radio = QButtonGroup()
        groupe_options_radio.addButton(self.option_radio_1)
        groupe_options_radio.addButton(self.option_radio_2)
        groupe_options_radio.addButton(self.option_radio_3)
        disposition.addWidget(groupe_options_2)


app = QApplication()
dbe = GroupeBoutonEx()
dbe.show()
app.exec()
