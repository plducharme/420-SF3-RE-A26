from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFrame, QVBoxLayout, QMenu,
                               QToolBar, QFileDialog, QMessageBox, QHBoxLayout, QCheckBox)
from todo import ToDo


class GestionnaireTache(QMainWindow):
    # Vue
    def __init__(self):
        super().__init__()

        self.cadre_principale = QFrame()
        disposition_principale = QVBoxLayout()
        self.cadre_principale.setLayout(disposition_principale)
        self.setWindowTitle("Gestionnaire de menu")
        self.setCentralWidget(self.cadre_principale)

        barre_menu = self.menuBar()

        menu_fichier = QMenu("&Fichier")
        action_ouvrir = QAction("Ouvrir", parent=self)
        action_ouvrir.triggered.connect(self.action_ouvrir_triggered)
        action_ouvrir.setIcon(QIcon("./images/open-folder.png"))
        menu_fichier.addAction(action_ouvrir)

        action_sauvegarder = QAction("&Sauvegarder", parent=self)
        action_sauvegarder.triggered.connect(self.action_sauvegarder_triggered)
        action_sauvegarder.setIcon(QIcon("./images/diskette.png"))
        menu_fichier.addAction(action_sauvegarder)

        menu_fichier.addSeparator()
        action_quitter = QAction("&Quitter", parent=self)
        action_quitter.triggered.connect(self.action_quitter_triggered)
        menu_fichier.addAction(action_quitter)

        barre_menu.addMenu(menu_fichier)

        barre_outils = QToolBar()
        barre_outils.addAction(action_ouvrir)
        barre_outils.addAction(action_sauvegarder)
        self.addToolBar(barre_outils)

        disposition_id = QHBoxLayout()
        libelle_id = QLabel("id:")
        self.todo_id = QLineEdit()
        self.todo_id.setInputMask("009")
        self.todo_id.textEdited.connect(self.todo_modifie)
        disposition_id.addWidget(libelle_id)
        disposition_id.addWidget(self.todo_id)
        disposition_principale.addLayout(disposition_id)

        disposition_description = QHBoxLayout()
        libelle_description = QLabel("Description:")
        self.todo_description = QLineEdit()
        self.todo_description.setMaxLength(250)
        self.todo_description.textEdited.connect(self.todo_modifie)
        disposition_description.addWidget(libelle_description)
        disposition_description.addWidget(self.todo_description)
        disposition_principale.addLayout(disposition_description)

        disposition_completee = QHBoxLayout()
        self.todo_completee = QCheckBox("Complétée?")
        self.todo_completee.clicked.connect(self.todo_modifie)
        disposition_completee.addWidget(self.todo_completee)
        disposition_principale.addLayout(disposition_completee)

        disposition_bouton_navigation = QHBoxLayout()
        self.bouton_precedent = QPushButton("Précédent")
        self.bouton_precedent.setEnabled(False)
        self.bouton_precedent.clicked.connect(self.bouton_precedent_clicked)
        disposition_bouton_navigation.addWidget(self.bouton_precedent)
        self.bouton_suivant = QPushButton("Suivant")
        self.bouton_suivant.setEnabled(False)
        self.bouton_suivant.clicked.connect(self.bouton_suivant_clicked)
        disposition_bouton_navigation.addWidget(self.bouton_suivant)
        disposition_principale.addLayout(disposition_bouton_navigation)

        # variables pour la gestion du modèle
        self.liste_todos = []
        self.modifiee = False
        self.index_todos = 0

    # Contrôleurs
    def bouton_precedent_clicked(self):
        self.index_todos -= 1
        self.afficher_todo(self.liste_todos[self.index_todos])
        if self.index_todos == 0:
            self.bouton_precedent.setEnabled(False)
        self.bouton_suivant.setEnabled(True)

    def bouton_suivant_clicked(self):
        self.index_todos += 1
        self.afficher_todo(self.liste_todos[self.index_todos])
        if self.index_todos == len(self.liste_todos) - 1:
            self.bouton_suivant.setEnabled(False)
        self.bouton_precedent.setEnabled(True)

    def action_ouvrir_triggered(self):
        chemin, filtre = QFileDialog.getOpenFileName(parent=self, caption="Choisir le json", dir=".", filter="fichier json (*.json)")

        if chemin:
            self.liste_todos = ToDo.charger_donnees(chemin)
            self.index_todos = 0
            if len(self.liste_todos) > 1:
                self.bouton_suivant.setEnabled(True)
                self.afficher_todo(self.liste_todos[0])
                self.modifiee = False

    def afficher_todo(self, todo: ToDo):
        self.todo_id.setText(str(todo.id))
        self.todo_description.setText(todo.description)
        self.todo_completee.setChecked(todo.completee)

    def action_quitter_triggered(self):
        if self.modifiee:
            dialogue_sauvegarder = QMessageBox()
            dialogue_sauvegarder.setText("Le document a été modifié.")
            dialogue_sauvegarder.setInformativeText("Voulez-vous sauvegarder vos modifications?")
            dialogue_sauvegarder.setStandardButtons(QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
            dialogue_sauvegarder.setDefaultButton(QMessageBox.StandardButton.Save)
            ret = dialogue_sauvegarder.exec()

            if ret == QMessageBox.StandardButton.Save:
                self.action_sauvegarder_triggered()
                self.close()
            elif ret == QMessageBox.StandardButton.Discard:
                self.close()
            else:
                return

    def action_sauvegarder_triggered(self):
        chemin, filtre = QFileDialog.getSaveFileName(parent=self, caption="Sauvegarder", dir=".", filter="fichier json (*.json)")
        if chemin:
            ToDo.sauvegarder_fichier(chemin, self.liste_todos)

    def todo_modifie(self):
        self.modifiee = True
        todo = self.liste_todos[self.index_todos]
        todo.id = int(self.todo_id.text())
        todo.description = self.todo_description.text()
        todo.completee = self.todo_completee.isChecked()


app = QApplication()
gt = GestionnaireTache()
gt.show()
app.exec()

