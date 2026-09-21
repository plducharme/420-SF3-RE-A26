from serie import Serie
from PySide6.QtWidgets import QApplication, QLabel, QComboBox, QLineEdit, QMainWindow, QWidget, QHBoxLayout, \
    QVBoxLayout, QGridLayout, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt


class GestionnaireSeries(QMainWindow):

    def __init__(self):
        super().__init__()

        self.series: list[Serie] = Serie.charger_donnees()

        self.setWindowTitle("Gestion Séries 2026")
        self.setWindowIcon(QIcon("icone.png"))

        self.widget_central = QWidget()
        self.disposition_principale = QVBoxLayout()
        self.widget_central.setLayout(self.disposition_principale)
        self.setCentralWidget(self.widget_central)

        self.disposition_selection = QHBoxLayout()
        self.libelle_selection = QLabel("Série: ")
        self.libelle_selection.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.disposition_selection.addWidget(self.libelle_selection)
        self.liste_selection = QComboBox()
        self.disposition_selection.addWidget(self.liste_selection)
        self.disposition_principale.addLayout(self.disposition_selection)

        for serie in self.series:
            # on ajoute l'item en utilisant le nom de la serie et on ajoute l'objet Serie lui-même
            self.liste_selection.addItem(serie.nom, serie)
        self.liste_selection.setCurrentIndex(0)

        self.liste_selection.currentIndexChanged.connect(self.liste_selection_changed)

        self.disposition_edition = QGridLayout()
        self.libelle_nom = QLabel("Nom:")
        self.input_nom = QLineEdit()
        self.libelle_annee_sortie = QLabel("Année de sortie:")
        self.input_annee_sortie = QLineEdit()
        self.input_annee_sortie.setInputMask("9999")
        self.libelle_nb_saisons = QLabel("Nombre de saisons:")
        self.input_nb_saisons = QLineEdit()
        self.input_nb_saisons.setInputMask("09")

        self.disposition_edition.addWidget(self.libelle_nom, 0, 0)
        self.disposition_edition.addWidget(self.input_nom, 0, 1)
        self.disposition_edition.addWidget(self.libelle_annee_sortie, 1, 0)
        self.disposition_edition.addWidget(self.input_annee_sortie, 1, 1)
        self.disposition_edition.addWidget(self.libelle_nb_saisons, 2, 0)
        self.disposition_edition.addWidget(self.input_nb_saisons, 2, 1)
        self.disposition_principale.addLayout(self.disposition_edition)

        self.afficher_info_serie(self.liste_selection.currentData())

        self.disposition_boutons = QHBoxLayout()
        self.bouton_sauvegarde = QPushButton()
        self.bouton_sauvegarde.setIcon(QIcon("sauvegarde.png"))
        self.bouton_sauvegarde.clicked.connect(self.bouton_sauvegarde_clicked)

        self.bouton_ajout = QPushButton()
        self.bouton_ajout.setIcon(QIcon("ajout.png"))
        self.bouton_ajout.clicked.connect(self.bouton_ajout_clicked)

        self.disposition_boutons.addWidget(self.bouton_sauvegarde)
        self.disposition_boutons.addWidget(self.bouton_ajout)
        self.disposition_principale.addLayout(self.disposition_boutons)

    def afficher_info_serie(self, serie: Serie):
        self.input_nom.setText(serie.nom)
        self.input_annee_sortie.setText(str(serie.annee_sortie))
        self.input_nb_saisons.setText(str(serie.nb_saisons))

    def liste_selection_changed(self, index: int):
        # self.afficher_info_serie(self.series[index])
        self.afficher_info_serie(self.liste_selection.currentData())

    def bouton_sauvegarde_clicked(self):
        serie = self.liste_selection.currentData()
        serie.nom = self.input_nom.text()
        serie.annee_sortie = int(self.input_annee_sortie.text())
        serie.nb_saisons = int(self.input_nb_saisons.text())

    def bouton_ajout_clicked(self):
        serie = Serie(self.input_nom.text(), int(self.input_annee_sortie.text()), int(self.input_nb_saisons.text()))
        self.liste_selection.addItem(serie.nom, serie)


app = QApplication()
gs = GestionnaireSeries()
gs.show()
app.exec()

