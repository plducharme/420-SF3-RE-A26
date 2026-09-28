from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QFileDialog, QFrame, QPushButton, QMenu, QProgressBar, \
    QToolBar, QApplication, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QAction, QIcon
from element_tableau import ElementTableauPeriodique


class TableauPeriodique(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Élements du tableau périodique")
        self.setWindowIcon(QIcon("./images/chemistry.png"))

        cadre_principal = QFrame()
        self.setCentralWidget(cadre_principal)

        # Menu
        self.barre_menu = self.menuBar()

        # Menu Fichier
        self.menu_fichier = QMenu("&Fichier")
        self.barre_menu.addMenu(self.menu_fichier)

        self.action_ouvrir = QAction("Ouvrir")
        self.action_ouvrir.setIcon(QIcon("./images/open-folder.png"))
        self.action_ouvrir.triggered.connect(self.action_ouvrir_triggered)

        self.action_enregistrer = QAction("Enregistrer")
        self.action_enregistrer.setIcon(QIcon("./images/diskette.png"))
        self.action_enregistrer.triggered.connect(self.action_enregistrer_triggered)

        self.action_quitter = QAction("Quitter")
        self.menu_fichier.addAction(self.action_ouvrir)
        self.menu_fichier.addAction(self.action_enregistrer)
        self.menu_fichier.addSeparator()
        self.menu_fichier.addAction(self.action_quitter)

        # Menu À propos
        self.menu_a_propos = QMenu("À propos")
        self.barre_menu.addMenu(self.menu_a_propos)
        self.action_a_propos = QAction("À propos")
        self.action_a_propos.triggered.connect(self.action_a_propos_triggered)
        self.menu_a_propos.addAction(self.action_a_propos)

        # Barre d'outils
        self.barre_outils = QToolBar()
        self.barre_outils.addAction(self.action_ouvrir)
        self.barre_outils.addAction(self.action_enregistrer)
        self.addToolBar(self.barre_outils)

        # Disposition principale
        disposition_principale = QVBoxLayout()
        cadre_principal.setLayout(disposition_principale)

        self.libelle_nom = QLabel("N/D")
        police_nom = self.libelle_nom.font()
        police_nom.setBold(True)
        police_nom.setPointSize(20)
        self.libelle_nom.setFont(police_nom)
        disposition_principale.addWidget(self.libelle_nom)

        self.libelle_symbole = QLabel("Symbole:")
        self.symbole_edit = QLineEdit()
        self.symbole_edit.textEdited.connect(self.element_modifie)
        disposition_symbole = QHBoxLayout()
        disposition_symbole.addWidget(self.libelle_symbole)
        disposition_symbole.addWidget(self.symbole_edit)
        disposition_principale.addLayout(disposition_symbole)

        self.libelle_numero_atomique = QLabel("Numéro Atomique:")
        self.numero_edit = QLineEdit()
        self.numero_edit.textEdited.connect(self.element_modifie)
        disposition_numero_atomique = QHBoxLayout()
        disposition_numero_atomique.addWidget(self.libelle_numero_atomique)
        disposition_numero_atomique.addWidget(self.numero_edit)
        disposition_principale.addLayout(disposition_numero_atomique)

        self.libelle_annee_decouverte = QLabel("Année Découverte:")
        self.edit_annee_decouverte = QLineEdit()
        self.edit_annee_decouverte.textEdited.connect(self.element_modifie)
        disposition_annee_decouverte = QHBoxLayout()
        disposition_annee_decouverte.addWidget(self.libelle_annee_decouverte)
        disposition_annee_decouverte.addWidget(self.edit_annee_decouverte)
        disposition_principale.addLayout(disposition_annee_decouverte)

        self.libelle_masse_atomique = QLabel("Masse atomique:")
        self.edit_masse_atomique = QLineEdit()
        self.edit_masse_atomique.textEdited.connect(self.element_modifie)
        disposition_masse_atomique = QHBoxLayout()
        disposition_masse_atomique.addWidget(self.libelle_masse_atomique)
        disposition_masse_atomique.addWidget(self.edit_masse_atomique)
        disposition_principale.addLayout(disposition_masse_atomique)

        disposition_boutons = QHBoxLayout()
        self.bouton_precedent = QPushButton("Précédent")
        self.bouton_precedent.setEnabled(False)
        self.bouton_precedent.clicked.connect(self.bouton_precedent_clicked)
        self.bouton_suivant = QPushButton("Suivant")
        self.bouton_suivant.setEnabled(False)
        self.bouton_suivant.clicked.connect(self.bouton_suivant_clicked)
        disposition_boutons.addWidget(self.bouton_precedent)
        disposition_boutons.addWidget(self.bouton_suivant)
        disposition_principale.addLayout(disposition_boutons)

        # Modèle
        self.elements_tableau = None
        self.elements_tableau_index = 0
        self.elements_modifiee = False

    def action_a_propos_triggered(self):
        QMessageBox.about(self, "À propos", "Éléments du tableau périodique\n\u00A92025")

    def bouton_precedent_clicked(self):
        self.elements_tableau_index -= 1
        self.afficher_element(self.elements_tableau_index)
        if self.elements_tableau_index == 0:
            self.bouton_precedent.setEnabled(False)
        if self.elements_tableau_index == len(self.elements_tableau) - 2:
            self.bouton_suivant.setEnabled(True)

    def bouton_suivant_clicked(self):
        self.elements_tableau_index += 1
        self.afficher_element(self.elements_tableau_index)
        if self.elements_tableau_index == len(self.elements_tableau) - 1:
            self.bouton_suivant.setEnabled(False)
        if self.elements_tableau_index == 1:
            self.bouton_precedent.setEnabled(True)

    def action_ouvrir_triggered(self):
        chemin, filtre = QFileDialog.getOpenFileName(parent=self, caption="Ouvrir un CSV", dir=".", filter="Fichier CSV (*.csv)")
        if chemin:
            self.elements_tableau = ElementTableauPeriodique.charger_donnees(chemin)
            self.afficher_element(0)
            if len(self.elements_tableau) > 1:
                self.bouton_suivant.setEnabled(True)

    def action_enregistrer_triggered(self):
        chemin, filtre = QFileDialog.getSaveFileName(parent=self, caption="Sélectionner le fichier à enregistrer", dir=".", filter="Fichier CSV (*.csv)")
        if chemin:
            ElementTableauPeriodique.enregistrer(chemin, self.elements_tableau)

    def afficher_element(self, index: int):
        element: ElementTableauPeriodique = self.elements_tableau[index]
        self.libelle_nom.setText(element.nom)
        self.symbole_edit.setText(element.symbole)
        self.numero_edit.setText(str(element.numero_atomique))
        self.edit_annee_decouverte.setText(str(element.annee_decouverte))
        self.edit_masse_atomique.setText(str(element.masse_atomique))

    def element_modifie(self):
        self.elements_modifiee = True
        element = ElementTableauPeriodique(int(self.numero_edit.text()), self.symbole_edit.text(), self.libelle_nom.text(), int(self.edit_annee_decouverte.text()), float(self.edit_masse_atomique.text()))
        self.elements_tableau[self.elements_tableau_index] = element

app = QApplication()
tp = TableauPeriodique()
tp.show()
app.exec()




