import os

from PySide6.QtCore import QSize, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QFileDialog
from PySide6.QtGui import QPixmap, QPainter, QColorConstants, QIcon
import glob


class BitmapAnimationAuto(QMainWindow):

    def __init__(self):
        super().__init__()
        self.disposition = QVBoxLayout()

        widget_central = QWidget()
        widget_central.setLayout(self.disposition)

        self.barre_outils = self.addToolBar("Barre d'outils")
        self.barre_outils.setIconSize(QSize(32, 32))
        self.bouton_ouvrir_fichier = QPushButton()
        icone_ouvrir_fichier = QIcon("./images/open-folder.png")
        self.bouton_ouvrir_fichier.setIcon(icone_ouvrir_fichier)
        self.bouton_ouvrir_fichier.clicked.connect(self.ouvrir_fichier)
        self.barre_outils.addWidget(self.bouton_ouvrir_fichier)

        self.etiquette = QLabel()
        self.canevas = QPixmap(800, 500)
        self.etiquette.setFixedSize(800, 500)
        self.canevas.fill(QColorConstants.White)
        self.etiquette.setPixmap(self.canevas)
        self.bouton_avancer = QPushButton("Start / Stop")
        self.bouton_avancer.clicked.connect(self.start_stop)
        self.disposition.addWidget(self.etiquette)
        self.disposition.addWidget(self.bouton_avancer)

        self.index_image = 0

        self.image_animee = None
        # On créé un timer qui émettra un signal de timeout après le temps configuré
        self.timer = QTimer()
        # On le connecte à la méthode qui sera constament rappelée
        self.timer.timeout.connect(self.animer)

        self.setCentralWidget(widget_central)

        self.nom_fichier = ""

    def start_stop(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            # Le timer émettra le signal "timeout" à chaque nombre de millisecondes spécifié
            self.timer.start(42)

    def animer(self):
        self.image_animee.dessiner(self.index_image)
        self.index_image += 1

    def ouvrir_fichier(self):
        self.nom_fichier = QFileDialog.getOpenFileName(self, "Ouvrir Image", "./images", "Images (*.png *.jpg)")
        prefixe_image = self.nom_fichier[0].split(".")[0]
        suffixe_image = self.nom_fichier[0].split(".")[-1]
        # Calcule le nombre d'images disponibles
        nombre_images = len(glob.glob(os.path.join("./images", prefixe_image + "_*." + suffixe_image)))

        self.image_animee = ImageAnimee(prefixe_image, suffixe_image, nombre_images, self)
        self.image_animee.dessiner(self.index_image)


class ImageAnimee:

    def __init__(self, prefixe_image: str, suffixe_image: str, nb_images: int, vue: BitmapAnimationAuto):
        self.prefixe_image = prefixe_image
        self.suffixe_image = suffixe_image
        self.nb_images = nb_images
        self.vue = vue
        self.liste_images = []
        for i in range(0, nb_images):
            self.liste_images.append(QPixmap(self.prefixe_image + "_" + str(i) + "." + self.suffixe_image))

    def pixmap(self, index: int):
        return self.liste_images[index % self.nb_images]

    def dessiner(self, index: int):
        canevas = self.vue.etiquette.pixmap()
        painter = QPainter(canevas)
        painter.drawPixmap(25, 25, self.pixmap(index))
        painter.end()
        self.vue.etiquette.setPixmap(canevas)


app = QApplication()
ba = BitmapAnimationAuto()
ba.show()
app.exec()
