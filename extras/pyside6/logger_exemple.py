from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QCheckBox, QButtonGroup
import logging


# Exemple de loggers. On configure un logger à un certain niveau (limite). Tous les messages que l'on log à un niveau
# supérieur à la limite auront un "output" dans la destination configurée (par défaut la console)
# DEBUG < INFO < WARNING < ERROR < CRITICAL
class DemoLogger(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemple loggers")
        # On le met au niveau DEBUG par défaut
        logging.getLogger().setLevel(logging.DEBUG)

        widget_central = QWidget()
        disposition = QGridLayout()
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        groupe_checkbox = QButtonGroup(self)
        groupe_checkbox.setExclusive(True)
        # groupe_checkbox.buttonClicked.connect(self)

        # Créer des cases à cocher pour sélectionner le niveau de log
        case_debug = QCheckBox("DEBUG")
        case_debug.setChecked(True)
        case_debug.clicked.connect(self.changer_niveau_logging)
        disposition.addWidget(case_debug, 0, 0)
        groupe_checkbox.addButton(case_debug)

        case_info = QCheckBox("INFO")
        case_info.clicked.connect(self.changer_niveau_logging)
        disposition.addWidget(case_info, 0, 1)
        groupe_checkbox.addButton(case_info)

        case_warning = QCheckBox("WARNING")
        case_warning.clicked.connect(self.changer_niveau_logging)
        disposition.addWidget(case_warning, 0, 2)
        groupe_checkbox.addButton(case_warning)

        case_error = QCheckBox("ERROR")
        case_error.clicked.connect(self.changer_niveau_logging)
        disposition.addWidget(case_error, 0, 3)
        groupe_checkbox.addButton(case_error)

        case_critical = QCheckBox("CRITICAL")
        case_critical.clicked.connect(self.changer_niveau_logging)
        disposition.addWidget(case_critical, 0, 4)
        groupe_checkbox.addButton(case_critical)

        # Les boutons pour générer des logs
        bouton_debug = QPushButton("message DEBUG")
        bouton_debug.clicked.connect(lambda: logging.debug("Message niveau DEBUG"))
        disposition.addWidget(bouton_debug, 1, 0, 1, 5)

        bouton_info = QPushButton("message INFO")
        bouton_info.clicked.connect(lambda: logging.info("Message niveau INFO"))
        disposition.addWidget(bouton_info, 2, 0, 1, 5)

        bouton_warning = QPushButton("message WARNING")
        bouton_warning.clicked.connect(lambda: logging.warning("Message niveau WARNING"))
        disposition.addWidget(bouton_warning, 3, 0, 1, 5)

        bouton_error = QPushButton("message ERROR")
        bouton_error.clicked.connect(lambda: logging.error("Message niveau ERROR"))
        disposition.addWidget(bouton_error, 4, 0, 1, 5)

        bouton_critical = QPushButton("message CRITICAL")
        bouton_critical.clicked.connect(lambda: logging.critical("Message niveau CRITICAL"))
        disposition.addWidget(bouton_critical, 5, 0, 1, 5)

    def changer_niveau_logging(self):
        case_cochee = self.sender()
        # selon la case coché, on veut
        match case_cochee.text():
            case "DEBUG":
                logging.getLogger().setLevel(logging.DEBUG)
            case "INFO":
                logging.getLogger().setLevel(logging.INFO)
            case "WARNING":
                logging.getLogger().setLevel(logging.WARNING)
            case "ERROR":
                logging.getLogger().setLevel(logging.ERROR)
            case "CRITICAL":
                logging.getLogger().setLevel(logging.CRITICAL)


app = QApplication()
dl = DemoLogger()
dl.show()
app.exec()
