from PySide6.QtCore import QObject, QVariantAnimation, QPointF, QEasingCurve, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QApplication


class PixmapAnimator(QObject):
    def __init__(self, item: QGraphicsPixmapItem, position_debut: QPointF, position_fin: QPointF,
                 duration: int = 2000, easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic, loop: bool = True):
        super().__init__()
        self.item = item
        self.debut = QPointF(position_debut)
        self.fin = QPointF(position_fin)
        self.anim = QVariantAnimation(self)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        self.anim.setDuration(duration)
        self.anim.setEasingCurve(QEasingCurve(easing))
        self.anim.valueChanged.connect(self._on_value)
        # Le nombre de fois que l'animation sera exécutée, -1 = infini
        self.anim.setLoopCount(-1 if loop else 1)

    def _on_value(self, v):
        # interpolation manuelle entre debut et fin
        x = self.debut.x() + (self.fin.x() - self.debut.x()) * float(v)
        y = self.debut.y() + (self.fin.y() - self.debut.y()) * float(v)
        self.item.setPos(QPointF(x, y))

    def play(self):
        self.anim.start()

    def pause(self):
        if self.anim.state() == self.anim.State.Running:
            self.anim.pause()

    def resume(self):
        if self.anim.state() == self.anim.State.Paused:
            self.anim.resume()

    def stop(self):
        self.anim.stop()


class FenetreAnimation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animation d'un pixmap avec un easing curve")
        largeur, hauteur = 800, 300

        self.scene = QGraphicsScene(0, 0, largeur, hauteur, self)
        self.view = QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)

        # charger et scaler le pixmap
        pix = QPixmap("./images/airplane.png")

        pix = pix.scaled(128, 64, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.item = QGraphicsPixmapItem(pix)
        self.scene.addItem(self.item)

        # point d'origine au centre pour rotations si besoin
        self.item.setTransformOriginPoint(pix.width() / 2, pix.height() / 2)

        start = QPointF(0, (hauteur - pix.height()) / 2)
        end = QPointF(largeur - pix.width(), (hauteur - pix.height()) / 2)

        # utilisez différents QEasingCurve.Type pour tester (InOutQuad, OutBounce, ElasticOut, ...)
        self.animator = PixmapAnimator(self.item, start, end, duration=2500, easing=QEasingCurve.Type.InOutCubic, loop=True)
        self.animator.play()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            # toggle pause / resume
            if self.animator.anim.state() == self.animator.anim.State.Running:
                self.animator.pause()
            elif self.animator.anim.state() == self.animator.anim.State.Paused:
                self.animator.resume()
        else:
            # Pour les touches non gérées, on appelle la méthode de la superclasse (comportement par défaut)
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication()
    fa = FenetreAnimation()
    fa.show()
    app.exec()
