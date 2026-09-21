from PySide6.QtWidgets import QApplication, QComboBox, QLabel, QVBoxLayout, QFrame
from PySide6.QtGui import QPixmap, QIcon


class ComboBoxData(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple de QComboBox avec Data")

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.image_canard = QPixmap("canard.png")
        self.image_eclair = QPixmap("lightning.png")

        self.combobox_data = QComboBox()
        self.combobox_data.addItem(QIcon("canard.png"), "canard", self.image_canard)
        self.combobox_data.addItem(QIcon("lightning.png"), "Éclair", self.image_eclair)
        self.combobox_data.currentIndexChanged.connect(self.combobox_data_index_changed)

        disposition.addWidget(self.combobox_data)

        self.libelle = QLabel()
        disposition.addWidget(self.libelle)

    def combobox_data_index_changed(self, index):
        data = self.combobox_data.currentData()
        self.libelle.setPixmap(data)


app = QApplication()
cbd = ComboBoxData()
cbd.show()
app.exec()
