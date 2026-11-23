from PySide6.QtWidgets import QFrame, QApplication, QLabel, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
import matplotlib
import matplotlib.pyplot as plt

# Dicte à matplotlib d'utiliser le canevas QT (FigureCanvasQTAgg) au lieu de générer une fenêtre séparée
matplotlib.use("Qt5Agg")


class OiseauxAvions(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accidents d'oiseaux avec les avions")

        self.disposition = QVBoxLayout()
        self.setLayout(self.disposition)

        self.canevas_mpl = FigureCanvasQTAgg()
        self.disposition.addWidget(self.canevas_mpl)

        self.barre_outils_mpl = NavigationToolbar2QT(self.canevas_mpl, self.canevas_mpl)

        # Créer notre figure matplotlib
        self.figure = plt.figure()

        coords_x = [x for x in range(10)]
        coords_y = [y**2 for y in range(10)]

        # pour ajouter plus d'un graphique sur une même figure, on utilise subplot()
        # 121 -> 1 ligne, 2 colonnes, position 1 (celui à gauche)
        plt.subplot(121)
        plt.bar(coords_x, coords_y, color="red")

        plt.title("y = x**2")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(["y = x**2"])

        # 122, 1 ligne, 2 colonnes, position 2 (celui de droite)
        plt.subplot(122)
        plt.plot(coords_x, coords_y, color="blue", linestyle="--", marker="*")
        plt.title("y = x**2")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend(["y = x**2"])
        self.canevas_mpl.figure = self.figure
        self.canevas_mpl.draw()


app = QApplication()
oa = OiseauxAvions()
oa.show()
app.exec()
