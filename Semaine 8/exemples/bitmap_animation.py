from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget
from PySide6.QtGui import QPixmap, QPainter, QColorConstants


class BitmapAnimation(QMainWindow):

    def __init__(self):
        super().__init__()
        self.disposition = QVBoxLayout()

        widget_central = QWidget()
        widget_central.setLayout(self.disposition)

        self.etiquette = QLabel()
        # On se déclare un canevas de 800 x 500
        self.canevas = QPixmap(800, 500)
        self.canevas.fill(QColorConstants.White)
        self.etiquette.setPixmap(self.canevas)
        self.bouton_avancer = QPushButton("Avancer")
        self.bouton_avancer.clicked.connect(self.avancer_clicked)
        self.disposition.addWidget(self.etiquette)
        self.disposition.addWidget(self.bouton_avancer)

        self.index_image = 0

        self.image_animee = ImageAnimee("./images/chat", 8, self)
        self.image_animee.dessiner(self.index_image)

        self.setCentralWidget(widget_central)

    def avancer_clicked(self):
        self.index_image += 1
        self.image_animee.dessiner(self.index_image)


class ImageAnimee:

    def __init__(self, prefixe_image: str, nb_images: int, vue: BitmapAnimation):
        self.prefixe_image = prefixe_image
        self.nb_images = nb_images
        self.vue = vue
        self.liste_images = []
        for i in range(0, nb_images):
            self.liste_images.append(QPixmap(self.prefixe_image + "_" + str(i) + ".png"))

    def pixmap(self, index: int):
        return self.liste_images[index % self.nb_images]

    def dessiner(self, index: int):
        canevas = self.vue.etiquette.pixmap()
        painter = QPainter(canevas)
        painter.drawPixmap(25, 25, self.pixmap(index))
        painter.end()
        self.vue.etiquette.setPixmap(canevas)


app = QApplication()
ba = BitmapAnimation()
ba.show()
app.exec()
