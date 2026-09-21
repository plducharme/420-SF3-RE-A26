from PySide6.QtWidgets import QVBoxLayout, QFrame, QLabel, QHBoxLayout, QRadioButton, QCheckBox, QApplication, \
    QComboBox, QButtonGroup, QPushButton, QProgressBar, QMessageBox, QLineEdit


class Quiz(QFrame):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz")

        disposition = QVBoxLayout()
        self.setLayout(disposition)

        self.questions_repondues = [False, False, False, False, False]

        # Question 1
        question1 = QLabel("Quelle est la capitale de la France?")
        disposition_question1 = QVBoxLayout()
        disposition_question1.addWidget(question1)
        disposition_reponses1 = QHBoxLayout()
        self.bouton_radio1 = QRadioButton("Paris")
        self.bouton_radio2 = QRadioButton("Londres")
        self.bouton_radio3 = QRadioButton("Berlin")
        self.bouton_group = QButtonGroup()
        self.bouton_group.addButton(self.bouton_radio1)
        self.bouton_group.addButton(self.bouton_radio2)
        self.bouton_group.addButton(self.bouton_radio3)
        self.bouton_group.buttonClicked.connect(self.question1_repondue)
        disposition_reponses1.addWidget(self.bouton_radio1)
        disposition_reponses1.addWidget(self.bouton_radio2)
        disposition_reponses1.addWidget(self.bouton_radio3)
        disposition_question1.addLayout(disposition_reponses1)
        disposition.addLayout(disposition_question1)

        # Question 2
        question2 = QLabel("Lesquels de ces aliments sont des fruits?")
        disposition_question2 = QVBoxLayout()
        disposition_question2.addWidget(question2)
        disposition_reponses2 = QHBoxLayout()
        self.checkbox1 = QCheckBox("Pomme")
        self.checkbox2 = QCheckBox("Carotte")
        self.checkbox3 = QCheckBox("Banane")
        self.button_group2 = QButtonGroup()
        self.button_group2.addButton(self.checkbox1)
        self.button_group2.addButton(self.checkbox2)
        self.button_group2.addButton(self.checkbox3)
        self.button_group2.buttonClicked.connect(self.question2_repondue)
        self.button_group2.setExclusive(False)
        disposition_reponses2.addWidget(self.checkbox1)
        disposition_reponses2.addWidget(self.checkbox2)
        disposition_reponses2.addWidget(self.checkbox3)
        disposition_question2.addLayout(disposition_reponses2)
        disposition.addLayout(disposition_question2)

        # Question 3
        question3 = QLabel("Quelle est la couleur du cheval blanc de Napoléon?")
        disposition_question3 = QVBoxLayout()
        disposition_question3.addWidget(question3)
        self.combo_box = QComboBox()
        self.combo_box.addItem("Noir")
        self.combo_box.addItem("Blanc")
        self.combo_box.addItem("Rouge")
        self.combo_box.currentIndexChanged.connect(self.question3_repondue)
        disposition_question3.addWidget(self.combo_box)
        disposition.addLayout(disposition_question3)

        # Question 4
        question4 = QLabel("Combien donne 2**8?")
        disposition_question4 = QVBoxLayout()
        disposition_question4.addWidget(question4)
        self.line_edit = QLineEdit("")
        disposition_question4.addWidget(self.line_edit)
        disposition.addLayout(disposition_question4)
        self.line_edit.editingFinished.connect(self.question4_repondue)

        # Question 5
        question5 = QLabel("Quelle est la monnaie officielle de l'Allemagne?")
        disposition_question5 = QVBoxLayout()
        disposition_question5.addWidget(question5)
        disposition_reponses5 = QHBoxLayout()
        self.bouton_radio_5_1 = QRadioButton("Euro")
        self.bouton_radio_5_2 = QRadioButton("Dollar")
        self.bouton_radio_5_3 = QRadioButton("Deutschmark")
        self.bouton_group_5 = QButtonGroup()
        self.bouton_group_5.addButton(self.bouton_radio_5_1)
        self.bouton_group_5.addButton(self.bouton_radio_5_2)
        self.bouton_group_5.addButton(self.bouton_radio_5_3)
        self.bouton_group_5.buttonClicked.connect(self.question5_repondue)
        disposition_reponses5.addWidget(self.bouton_radio_5_1)
        disposition_reponses5.addWidget(self.bouton_radio_5_2)
        disposition_reponses5.addWidget(self.bouton_radio_5_3)
        disposition_question5.addLayout(disposition_reponses5)
        disposition.addLayout(disposition_question5)

        # QProgressBar
        self.barre_progression = QProgressBar()
        disposition.addWidget(self.barre_progression)
        self.barre_progression.setMaximum(5)
        self.barre_progression.setValue(0)

        # Bouton pour valider les réponses
        bouton_valider = QPushButton("Valider")
        disposition.addWidget(bouton_valider)
        bouton_valider.clicked.connect(self.valider_reponses)

    def question1_repondue(self):
        if not self.questions_repondues[0]:
            self.questions_repondues[0] = True
            self.barre_progression.setValue(self.barre_progression.value()+1)

    def question2_repondue(self):
        if not self.questions_repondues[1]:
            self.questions_repondues[1] = True
            self.barre_progression.setValue(self.barre_progression.value()+1)

    def question3_repondue(self):
        if not self.questions_repondues[2]:
            self.questions_repondues[2] = True
            self.barre_progression.setValue(self.barre_progression.value()+1)

    def question4_repondue(self):
        if not self.questions_repondues[3]:
            self.questions_repondues[3] = True
            self.barre_progression.setValue(self.barre_progression.value()+1)

    def question5_repondue(self):
        if not self.questions_repondues[4]:
            self.questions_repondues[4] = True
            self.barre_progression.setValue(self.barre_progression.value()+1)

    def valider_reponses(self):
        dialog = QMessageBox()
        dialog.setWindowTitle("Résultat")
        resultats = "Résultats:\n"
        if self.bouton_radio1.isChecked():
            resultats += "Question 1: Correct\n"
        else:
            resultats += "Question 1: Incorrect\n"
        if self.checkbox1.isChecked() and self.checkbox3.isChecked() and not self.checkbox2.isChecked():
            resultats += "Question 2: Correct\n"
        else:
            resultats += "Question 2: Incorrect\n"
        if self.combo_box.currentText() == "Blanc":
            resultats += "Question 3: Correct\n"
        else:
            resultats += "Question 3: Incorrect\n"
        if self.line_edit.text() == "256":
            resultats += "Question 4: Correct\n"
        else:
            resultats += "Question 4: Incorrect\n"
        if self.bouton_radio_5_1.isChecked():
            resultats += "Question 5: Correct\n"
        else:
            resultats += "Question 5: Incorrect\n"
        dialog.setText(resultats)
        dialog.exec()


app = QApplication()
quiz = Quiz()
quiz.show()
app.exec()




