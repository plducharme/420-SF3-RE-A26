from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
from PySide6.QtGui import QAction, QIcon


class MenuCochable(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de menu QAction Cochable")

        self.barre_de_menu = QMenuBar()
        self.setMenuBar(self.barre_de_menu)

        self.menu_selection = QMenu()
        self.menu_selection.setTitle("&Sélection")
        self.barre_de_menu.addMenu(self.menu_selection)

        self.action_rouge = QAction(parent=self)
        self.action_rouge.setText("Rouge")
        self.icone_rouge = QIcon("carre_rouge.png")
        self.action_rouge.setIcon(self.icone_rouge)
        self.action_rouge.setCheckable(True)
        self.action_rouge.toggled.connect(self.rouge_coche)
        self.menu_selection.addAction(self.action_rouge)

        self.menu_selection.addSeparator()

        self.action_vert = QAction(parent=self)
        self.action_vert.setText("Vert")
        self.icone_verte = QIcon("carre_vert.png")
        self.action_vert.setIcon(self.icone_verte)
        self.action_vert.triggered.connect(self.vert_clique)
        self.menu_selection.addAction(self.action_vert)

    @staticmethod
    def vert_clique(self):
        print("Click, click, boom!")

    def rouge_coche(self):
        if self.action_rouge.isChecked():
            print("Rouge coché")
        else:
            print("Rouge décoché")


application = QApplication()
mc = MenuCochable()
mc.show()
application.exec()


