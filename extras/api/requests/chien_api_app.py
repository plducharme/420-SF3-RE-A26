from PySide6.QtCore import QSize
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QApplication, QHBoxLayout, QComboBox, QPushButton
from PySide6.QtGui import QPixmap

from chien_api_client import ChienApiClient


class ChienApiApp(QFrame):
    def __init__(self):
        super().__init__()

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.setWindowTitle("Images de chiens")

        self.libelle_image = QLabel()
        self.libelle_image.setPixmap(QPixmap(QSize(600, 600)))

        self.disposition.addWidget(self.libelle_image)

        self.disposition_breeds = QHBoxLayout()
        self.bouton_all_breeds = QPushButton("Lister races")
        self.bouton_all_breeds.clicked.connect(self.bouton_all_breeds_clicked)

        self.disposition_selection_image = QVBoxLayout()

        self.liste_breeds = QComboBox()
        self.liste_breeds.setDisabled(True)
        self.liste_breeds.currentIndexChanged.connect(self.liste_breeds_current_index_changed)
        self.disposition_selection_image.addWidget(self.liste_breeds)

        self.liste_images = QComboBox()
        self.liste_images.setDisabled(True)
        self.liste_images.currentIndexChanged.connect(self.liste_images_current_index_changed)

        self.disposition_selection_image.addWidget(self.liste_images)

        self.disposition_breeds.addWidget(self.bouton_all_breeds)
        self.disposition_breeds.addLayout(self.disposition_selection_image)
        self.disposition.addLayout(self.disposition_breeds)

    def bouton_all_breeds_clicked(self):
        self.liste_breeds.clear()
        self.liste_breeds.addItems(ChienApiClient.get_all_breeds().keys())
        self.liste_breeds.setDisabled(False)

    def liste_breeds_current_index_changed(self, index):
        breed = self.liste_breeds.currentText()
        self.liste_images.clear()
        self.liste_images.addItems(ChienApiClient.get_images_url_by_breed(breed))
        self.liste_images.setDisabled(False)

    def liste_images_current_index_changed(self, index):
        url = self.liste_images.currentText()
        if url == "":
            return
        pixmap = QPixmap()
        pixmap.loadFromData(ChienApiClient.get_image_data(url))
        # Si l'image est trop grande, on la redimensionne
        if pixmap.size().width() > 600 or pixmap.size().height() > 600:
            proportion = pixmap.width() / pixmap.height()
            pixmap = pixmap.scaled(600, 600 / proportion)
        self.libelle_image.setPixmap(pixmap)


app = QApplication()
ca = ChienApiApp()
ca.show()
app.exec()

