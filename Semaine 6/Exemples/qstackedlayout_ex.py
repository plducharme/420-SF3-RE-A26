from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QStackedLayout, QComboBox, QLabel, QPushButton
from PySide6.QtCore import Qt


class QStackedLayoutEx(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple QStackedLayout")

        self.disposition_verticale = QVBoxLayout()
        self.setLayout(self.disposition_verticale)
        self.choix_page_combo = QComboBox()
        self.disposition_empilee = QStackedLayout()
        # En StackAll, tous les contenus sont visibles, mais celui sélectionné est par-dessus les autres
        self.disposition_empilee.setStackingMode(QStackedLayout.StackingMode.StackAll)

        self.choix_page_combo.currentIndexChanged.connect(self.disposition_empilee.setCurrentIndex)
        self.disposition_verticale.addWidget(self.choix_page_combo)

        self.libelle_droite = QLabel("Texte à droite")
        self.libelle_droite.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.choix_page_combo.addItem("texte à droite")
        self.disposition_empilee.addWidget(self.libelle_droite)

        self.libelle_gauche = QLabel("Texte à gauche")
        self.choix_page_combo.addItem("Texte à gauche")
        self.disposition_empilee.addWidget(self.libelle_gauche)

        self.libelle_haut = QLabel("Texte en haut")
        self.libelle_haut.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.choix_page_combo.addItem("Texte en haut")
        self.disposition_empilee.addWidget(self.libelle_haut)

        bouton_1 = QPushButton("Bouton 1")
        self.disposition_empilee.addWidget(bouton_1)
        self.choix_page_combo.addItem("Bouton 1")
        # Comme les layouts sont empilés, les autres libellés ne pourront être plus petit que la grandeur du bouton
        bouton_1.setMinimumSize(500, 500)

        self.disposition_verticale.addLayout(self.disposition_empilee)


app = QApplication()
qsle = QStackedLayoutEx()
qsle.show()
app.exec()