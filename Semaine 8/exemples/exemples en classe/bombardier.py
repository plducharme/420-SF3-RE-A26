from PySide6.QtWidgets import (QApplication, QGraphicsPixmapItem, QFrame, QVBoxLayout, QGraphicsView, QGraphicsScene,
                               QMessageBox, QPushButton)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect, QPoint, QSize, QPointF, Qt, QTimer
import random


class Bombardier(QFrame):

    GRANDEUR_RECT = QRect(0, 0, 800, 800)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bombardier 2026")
        self.resize(QSize(Bombardier.GRANDEUR_RECT.width() + 50, Bombardier.GRANDEUR_RECT.height() + 50))

        self.disposition = QVBoxLayout()
        self.vue = QGraphicsView()
        self.setLayout(self.disposition)
        self.disposition.addWidget(self.vue)

        self.bouton_recommencer = QPushButton("Recommencer")
        self.bouton_recommencer.clicked.connect(self.bouton_recommencer_clicked)
        self.disposition.addWidget(self.bouton_recommencer)

        self.scene = QGraphicsScene()
        self.vue.setScene(self.scene)

        self.jeu = BombardierJeu(self.scene, Bombardier.GRANDEUR_RECT)

        self.timer = QTimer()
        self.timer.timeout.connect(self.mise_a_jour_jeu)
        self.timer.setInterval(50)
        self.timer.start()

    def mise_a_jour_jeu(self):
        match self.jeu.etat:
            case self.jeu.ETAT_EN_COURS:
                self.jeu.mise_a_jour_jeu()
                self.vue.setScene(self.jeu.scene)
            case self.jeu.ETAT_PERDU:
                QMessageBox.information(self, "Perdu!", "Vous avez manqué la cible")
                self.jeu.etat = self.jeu.ETAT_EN_PAUSE
            case self.jeu.ETAT_GAGNE:
                QMessageBox.information(self, "Gagné!", "Bravo, vous êtes un maître des airs")
                self.jeu.etat = self.jeu.ETAT_EN_PAUSE
            case _:
                pass

    def keyPressEvent(self, event, /):
        if event.key() == Qt.Key.Key_B:
            self.jeu.generer_bombe()
        else:
            super().keyPressEvent(event)

    def bouton_recommencer_clicked(self):
        self.scene = QGraphicsScene()
        self.vue.setScene(self.scene)
        self.jeu = BombardierJeu(self.scene, Bombardier.GRANDEUR_RECT)


class BombardierJeu:
    VITESSE_BOMBARDIER = 10
    GRAVITE = 20

    ETAT_EN_COURS = 0
    ETAT_GAGNE = 1
    ETAT_PERDU = 2
    ETAT_EN_PAUSE = 3

    def __init__(self, scene: QGraphicsScene, grandeur_jeu: QRect):
        self.scene = scene
        self.scene.setSceneRect(grandeur_jeu)
        self.grandeur_jeu = grandeur_jeu
        self.bombardier = ObjetJeu(QPixmap("../images/airplane.png"), QPoint(10, 10), QSize(100, 100))
        self.cible = ObjetJeu(QPixmap("../images/target.png"), QPoint(random.randint(400, 775), 725), QSize(64, 64))
        self.bombe: QGraphicsPixmapItem | None = None

        self.scene.addItem(self.bombardier)
        self.scene.addItem(self.cible)
        self.etat = BombardierJeu.ETAT_EN_COURS

    def generer_bombe(self):
        if self.bombe is None:
            self.bombe: QGraphicsPixmapItem = ObjetJeu(QPixmap("../images/nuclear-bomb.png"),
                                                       self.bombardier.pos().toPoint(), QSize(64, 64))
            self.scene.addItem(self.bombe)

    def verifier_collision(self):
        if self.bombe and self.bombe.collidesWithItem(self.cible):
            self.etat = BombardierJeu.ETAT_GAGNE

    def mise_a_jour_jeu(self):
        # Fait avancer le bombardier
        self.bombardier.setPos(QPointF(self.bombardier.pos().x() + BombardierJeu.VITESSE_BOMBARDIER,
                                       self.bombardier.pos().y()))
        if self.bombe is not None:
            self.bombe.setPos(QPointF(self.bombe.pos().x() + BombardierJeu.VITESSE_BOMBARDIER,
                                      self.bombe.pos().y() + BombardierJeu.GRAVITE))

        self.verifier_collision()
        if self.bombardier.pos().x() > self.grandeur_jeu.size().width():
            self.etat = BombardierJeu.ETAT_PERDU


class ObjetJeu(QGraphicsPixmapItem):

    def __init__(self, pixmap: QPixmap, position: QPoint, grandeur: QSize):
        super().__init__(pixmap.scaled(grandeur))
        self.setPos(position)


app = QApplication()
bombardier = Bombardier()
bombardier.show()
app.exec()
