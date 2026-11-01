from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsTextItem
from PySide6.QtGui import QPen, QBrush, QColor, QPixmap, QFont
from PySide6.QtCore import Qt, QRect


class GraphicsBase(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(QRect(0, 0, 400, 400))
        # notre classe hérite du QGraphicsView, on lui assigne la scene créée
        self.setScene(self.scene)

        crayon = QPen(QColor("blue"))
        pinceau = QBrush(QColor("lightblue"))
        # Ajoute un rectangle à la scene
        self.scene.addRect(50, 50, 100, 100, crayon, pinceau)

        pix = QPixmap("./images/airplane.png")

        pix = pix.scaled(128, 128, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        graphics_pixmap = QGraphicsPixmapItem(pix)
        graphics_pixmap.setPos(QPoint(90, 90))
        # Les addQuelqueChose() ajoute à la scène et retourne l'objet ajouté
        texte: QGraphicsTextItem = self.scene.addText("Texte en deux dimensions")
        police = QFont()
        police.setBold(True)
        texte.setFont(police)
        texte.setPos(QPoint(100, 300))
        # addItem(QGraphicsItem) ajoute un QGraphics Item déjà défini
        self.scene.addItem(graphics_pixmap)


app = QApplication()
gb = GraphicsBase()
gb.show()
app.exec()

