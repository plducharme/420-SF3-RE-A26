from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
from PySide6.QtGui import QAction


class MaBarreDeMenuEx(QMainWindow):

    def __init__(self):
        super().__init__()
        barre_de_menu1 = QMenuBar()

        menu_test = QMenu("Test")
        action_fermer = QAction(parent=self)
        action_fermer.setText("Fermer l'application")
        action_fermer.triggered.connect(self.close)
        menu_test.addAction(action_fermer)

        action_changer_menu = QAction(parent=self)
        action_changer_menu.setText("Changer le menu")
        action_changer_menu.triggered.connect(self.action_menu_changer)
        menu_test.addAction(action_changer_menu)

        self.barre_de_menu2 = QMenuBar()
        menu_change = QMenu("Autre Menu")
        menu_change.addAction(action_fermer)
        self.barre_de_menu2.addMenu(menu_change)

        barre_de_menu1.addMenu(menu_test)
        self.setMenuBar(barre_de_menu1)

    def action_menu_changer(self):
        self.setMenuBar(self.barre_de_menu2)


app = QApplication()
mbm = MaBarreDeMenuEx()
mbm.show()
app.exec()
