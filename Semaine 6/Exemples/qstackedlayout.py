from PySide6.QtWidgets import QStackedLayout, QApplication, QMainWindow, QComboBox, QWidget, QLabel, QVBoxLayout


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        self.disposition_stacked = QStackedLayout()
        disposition_vbox = QVBoxLayout()
        widget_central.setLayout(disposition_vbox)

        self.liste_pages = QComboBox()
        self.liste_pages.addItem("Page 1")
        self.liste_pages.addItem("Page 2")
        self.liste_pages.addItem("Page 3")

        self.liste_pages.currentIndexChanged.connect(self.index_change)

        page1 = QLabel("Page 1\nBonjour")
        page2 = QLabel("Page 2\nBonsoir")
        page3 = QLabel("Page 3\nBonne nuit!")

        self.disposition_stacked.addWidget(page1)
        self.disposition_stacked.addWidget(page2)
        self.disposition_stacked.addWidget(page3)

        disposition_vbox.addWidget(self.liste_pages)
        disposition_vbox.addLayout(self.disposition_stacked)
        
        self.setCentralWidget(widget_central)

    def index_change(self):
        index = self.liste_pages.currentIndex()
        self.disposition_stacked.setCurrentIndex(index)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()