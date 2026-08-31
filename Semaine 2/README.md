# Bases des éléments d'une fenêtre
1) Créer une application PySide6
   1) Qui affiche un titre "Mon application"
   2) Qui contient une barre de statut
   3) Qui contient deux menus "&Menu1" et "M&enu2" avec chacun leur QAction 
      1) Lorsque l'on clique "Menu1", affichera le conseil dans la barre de statut "Menu1" (setStatusTip())
      2) Lorsque l'on clique le QAction du "Menu2", affichera le conseil "Menu2" dans la barre de statut (setStatusTip())
      3) Remarquer l'effet des "&" sur les noms des menus
      4) Ajouter des QAction à chaque menu
   4) Qui contient une barre d'outils
      1) Ajouter un QPushButton à la barre d'outils
         1) Faire un print() à la console lorsque pesé
   5) Qui contient un QWidget avec un QVBoxLayout avec
      1) un QPushButton
         1) Qui ouvrira un QDialog
            1) Contiendra un layout avec un QPushButton qui fermera le QDialog

# Lecteur de GIFs 

Un GIF (Graphic Interchange Format) est une image bitmap qui est animée. En regardant la documentation de
[QLabel](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QLabel.html#qlabel), l'on peut voir que le contenu supporté 
inclus [QMovie](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QMovie.html#qmovie).

Les [QAction](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QAction.html#qaction) peuvent être affichées sous formes
d'icônes en utilisant un [QIcon](https://doc.qt.io/qtforpython-6/PySide6/QtGui/QIcon.html#qicon) 

1) Créer une application PySide6
   1) La fenêtre principale aura comme titre "Lecteur de GIFs"
   2) Créer une QAction action_jouer
      1) ayant l'icône "jouer.png"
      2) connectée à une méthode jouer(self) qui activera le GIF
   3) Créer une QAction action_stop
      1) ayant l'icône "stop.png"
      2) connectée à une méthode stop(self) qui arrêtera l'animation du GIF
   4) Ajouter un QLabel à la fenêtre (idéalement dans un QVBoxLayout)
   5) Initialiser un QMovie avec le GIF "sup.gif"
      1) L'assigner au QLabel
      2) L'activer par défaut
   6) Ajouter un menu contenant les deux actions
   7) Ajouter barre d'outils avec les deux actions
