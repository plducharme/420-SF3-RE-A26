from PySide6.QtWidgets import QApplication, QFrame, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap, QMovie


class VisualisateurImage(QFrame):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Visualisateur d'image")
        # Utilisation d'un QPixmap comme icône
        self.icone_oeil = QPixmap("../images/oeil.png")
        self.setWindowIcon(self.icone_oeil)
        # Initialisation d'un QPixmap
        self.image = QPixmap("../images/fantome.png")
        # Les gifs sont considérés comme des films
        self.gif = QMovie("../images/zombies.gif")
        self.gif.start()

        self.libelle_image = QLabel()
        self.libelle_image.setPixmap(self.image)

        self.libelle_gif = QLabel()
        self.libelle_gif.setMovie(self.gif)

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.disposition.addWidget(self.libelle_image)
        self.disposition.addWidget(self.libelle_gif)


if __name__ == "__main__":
    app = QApplication()
    visualisateur_image = VisualisateurImage()
    visualisateur_image.show()
    app.exec()

