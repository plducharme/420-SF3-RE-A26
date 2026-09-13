from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QPushButton, QVBoxLayout, QFontDialog


# icone stylo: <a href="https://www.flaticon.com/free-icons/ballpoint" title="ballpoint icons">Ballpoint icons created by Smashicons - Flaticon</a>

class CadreEx(QFrame):

    def __init__(self):
        super().__init__()

        self.setFrameStyle(QFrame.Shape.WinPanel | QFrame.Shadow.Raised)



        disposition = QVBoxLayout()
        self.setLayout(disposition)

        libelle_texte = QLabel("Texte brute")
        disposition.addWidget(libelle_texte)

        libelle_riche_police = QLabel()
        libelle_riche_police.setText("Police pour le libellé en entier")
        police = QFont()
        police.setFamily("Cambria")
        police.setItalic(True)
        police.setPointSize(16)
        libelle_riche_police.setFont(police)
        disposition.addWidget(libelle_riche_police)

        libelle_html = QLabel()
        libelle_html.setText("""La <b>documentation</b> de <i>QLabel</i> est disponible 
        <a href="https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLabel.html#PySide6.QtWidgets.QLabel">ici (externe)</a>             
        """)
        libelle_html.setOpenExternalLinks(True)
        disposition.addWidget(libelle_html)

        libelle_qss = QLabel()
        libelle_qss.setText("""<p style="font-size:18px;color:#BF80FF;">Ceci est un texte stylé</p>""")
        disposition.addWidget(libelle_qss)

        self.libelle_options = QLabel()
        self.libelle_options.setText("Ah que la neige a neigé!")
        disposition.addWidget(self.libelle_options)

        bouton_selection_police = QPushButton()
        icone_stylo = QIcon("./pen.png")
        bouton_selection_police.setIcon(icone_stylo)
        bouton_selection_police.clicked.connect(self.bouton_selection_police_clicked)
        disposition.addWidget(bouton_selection_police)


    def bouton_selection_police_clicked(self):
        ok, police_selectionnee = QFontDialog.getFont(self)
        if ok:
            self.libelle_options.setFont(police_selectionnee)


app = QApplication()
ce = CadreEx()
ce.show()
app.exec()
