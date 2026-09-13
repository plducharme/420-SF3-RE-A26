from PySide6.QtWidgets import QApplication, QFrame, QLabel, QPushButton, QVBoxLayout, QFontDialog, QFileDialog
from PySide6.QtGui import QPixmap, QFont, QIcon
from PySide6.QtCore import QSize

# Icône provenant de <a href="https://www.flaticon.com/free-icons/ballpoint" title="ballpoint icons">Ballpoint icons created by Smashicons - Flaticon</a>

class StylesExemple(QFrame):
    def __init__(self):
        super().__init__()

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Sunken)
        self.setBaseSize(QSize(800, 600))

        libelle_plain = QLabel()
        libelle_plain.setText("Ceci est un texte brute")
        libelle_plain.setFrameShadow(QFrame.Shadow.Raised)
        disposition.addWidget(libelle_plain)

        libelle_riche = QLabel()
        libelle_riche.setText("Ceci est un texte riche")
        police_libelle_riche = QFont()
        police_libelle_riche.setFamily("Calibri")
        police_libelle_riche.setPointSize(24)
        libelle_riche.setFont(police_libelle_riche)
        disposition.addWidget(libelle_riche)

        bouton_police_dialogue = QPushButton()
        bouton_police_dialogue_icone = QIcon("pen.png")
        bouton_police_dialogue.setIcon(bouton_police_dialogue_icone)
        bouton_police_dialogue.clicked.connect(self.bouton_police_dialogue_clicked)
        disposition.addWidget(bouton_police_dialogue)

        self.libelle_variant = QLabel()
        self.libelle_variant.setText("Il était une fois")
        disposition.addWidget(self.libelle_variant)

        self.libelle_image = QLabel()
        self.libelle_image.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Raised)
        self.libelle_image.setLineWidth(3)
        disposition.addWidget(self.libelle_image)

        bouton_image_dialogue = QPushButton("Choisir une image")
        bouton_image_dialogue.clicked.connect(self.bouton_image_dialogue_clicked)
        disposition.addWidget(bouton_image_dialogue)

        libelle_riche_html = QLabel()
        libelle_riche_html.setText("""
                            <b>texte stylé</b>
                            <p style="color:#6699FF;font-size:18px;font-style:italic;">
                                   Le souvenir est le parfum de l'âme.</p>
                                   """)
        disposition.addWidget(libelle_riche_html)

    def bouton_police_dialogue_clicked(self):
        # Ouvre la boîte de dialogue pour choisir une police
        ok, police = QFontDialog.getFont(self.libelle_variant.font(), self, "Choisissez une police")
        if ok:  # Si l'utilisateur valide
            self.libelle_variant.setFont(police)  # Applique la police sélectionnée au QLabel

    def bouton_image_dialogue_clicked(self):
        chemin_image, filtre = QFileDialog.getOpenFileName(self, "Choisir une image", "./images", "Ficher Images (*.png)")
        self.libelle_image.setPixmap(QPixmap(chemin_image))


app = QApplication()
se = StylesExemple()
se.show()
app.exec()

