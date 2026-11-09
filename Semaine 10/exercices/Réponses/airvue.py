from datetime import datetime
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout, \
    QComboBox, QMenu, QFrame
from PySide6.QtGui import QPixmap, QAction
import sqlite3


class AirVue(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Super Duper Air Machin Truc 2026")
        self.air_pixmap = QPixmap("air.png")
        self.setWindowIcon(self.air_pixmap)

        self.menu_fichier = QMenu("Fichier")
        self.barre_menu = self.menuBar()
        self.barre_menu.addMenu(self.menu_fichier)

        self.action_exporter_pdf = QAction("Exporter vers un PDF")
        self.menu_fichier.addAction(self.action_exporter_pdf)

        self.menu_fichier.addSeparator()

        self.action_quitter = QAction("Quitter")
        self.action_quitter.triggered.connect(self.close)
        self.action_quitter.setShortcut("Ctrl+Q")
        self.menu_fichier.addAction(self.action_quitter)

        self.disposition_principale = QVBoxLayout()
        self.widget_principal = QFrame()
        self.widget_principal.setLayout(self.disposition_principale)
        self.setCentralWidget(self.widget_principal)

        self.donnees: list[Mesure] = self.import_donnees_pandas()
        print()

    @staticmethod
    def import_donnees_pandas() -> list[Mesure]:
        # initie une connection à sqlite
        con = sqlite3.connect("airdata.sqlite")
        query = "SELECT * FROM mesures"
        df = pd.read_sql_query(query, con)
        mesures: list[Mesure] = []
        for idx, series in df.iterrows():
            mesures.append(Mesure(series["timestamp"], series["temperature_c"], series["humidity_pct"], series["co2_ppm"], series["voc_ppb"], series["radon_bq_m3"], series["pm25_ug_m3"], series["pressure_hpa"]))
        return mesures

class Mesure:

    def __init__(self, date: datetime, temperature: float, humidite: float, co2: int, cov: int, radon: float, pm25:float, pression: float):
        self.date_echantillon = date
        self.temperature = temperature
        self.humidite = humidite
        self.co2 = co2
        self.cov = cov
        self.radon = radon
        self.pm25 = pm25
        self.pression = pression


if __name__ == "__main__":
    app = QApplication()
    av = AirVue()
    av.show()
    app.exec()
