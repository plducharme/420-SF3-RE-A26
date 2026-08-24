Exercices

# Tkinter
1) Créer une application Tkinter
   1) qui affiche une fenêtre avec le titre "Sagesse"
   2) qui contient un Label: "Ils ne sont grands que parce que nous sommes à genoux. -La Boétie"
   3) qui possède un Button qui ferme la fenêtre
2) Qu'arrive-t-il si vous ajoutez des retours de lignes "\n" dans la phrase du Label?
3) Ajouter une fonction qui retournera une citation prise au hasard dans le fichier citations.txt
   1) Les exemples de lectures de fichiers sont dans le dépôt PythonExercices
   4) Utiliser cette fonction pour créer le Label
   5) Ajouter une logique qui permettra d'ajouter les "\n" à chaque 3 mots et avant l'auteur.

# PySide
1) À partir de l'exemple des notes de cours, recréer une fenêtre
   1) contenant simplement un bouton qui fermera la fenêtre
   2) changer la méthode connectée pour ajouter une nouvelle méthode "handle_button_ok"
      1) dans la méthode, faire un output "click!" vers la console
      2) créer un QLabel qui affiche "Cliquez pour une équation"
      3) Ajouter le label et le bouton précédent à un QVBoxLayout comme ceci:
      
      >main_layout = QVBoxLayout()
      main_layout.addWidget(<variable du label>)
      main_layout.addWidget(<variable du bouton>)
   
      >main_container = QWidget()
      main_container.setLayout(main_layout)
   
      >self.setCentralWidget(main_container)
   3) Ajouter la logique dans la méthode pour afficher une équation au hasard au lieu de fermer la fenêtre

Documentation officielle PySide6: https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/



