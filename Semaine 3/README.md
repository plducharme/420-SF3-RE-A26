# Stylage de cadres
1) Créer une application avec un QVBoxLayout contenant 
   1) un QMenu avec deux QAction
   2) un QLabel contenant du texte riche
   3) un QLabel contenant l'image 'ex1.png'
2) Pour chaque widget ajouté, essayez les divers styles de cadre (setFrameStyle) et voyez l'effet


# Jouons avec les boutons et le texte
1) Créer une application avec un QVBoxLayout contenant
   1) un QLabel contenant le texte suivant: `"L'informatique, ça fait gagner beaucoup de temps... à condition d'en avoir beaucoup devant soi !"`
   2) un bouton qui permettra de rendre le texte en italique ou d'enlever l'italique
   3) un bouton qui permettra d'appliquer les caractères gras ou de les enlever
   4) un bouton qui permettra d'activer ou désactivé le "wordWrap"
   5) un bouton qui va augmenter la police
   6) un bouton qui va diminuer la police
   7) un bouton qui va désactiver/activer tous les autres boutons
   8) connecter une méthode pressed et release d'un bouton et ajouter un output à la console, regarder ce qui arrive lorsque vous cliquez sans relâcher et lorsque vous relâchez
   9) ajouter un bouton qui va afficher un QDialog avec le texte sélectionné dans le QLabel. Si aucun texte est sélectionné, afficher "Sélectionner du texte de la citation"
      1) Pour faire fonctionner ceci, ajouter un raccourci clavier et utiliser le raccourci clavier après avoir sélectionné


# Affichons des données à partir d'un csv
1) Créer une application qui permettra d'afficher les informations contenu dans le fichier times.csv
2) Utiliser des QLabel pour créer le UI qui va afficher les éléments d'une ligne du fichier
3) L'application aura un bouton qui permettra d'afficher la ligne précédente et un bouton qui permettra d'afficher la ligne suivante
   1) S'il n'y a pas de ligne précédente, le bouton "Précédent" devra être désactivé (et réactivé si de nouveau disponible)
   2) S'il n'y a pas de ligne suivante, le bouton "Suivant" devra être désactivé (et réactivé si de nouveau disponible)
4) Si vous avez du temps, ajouter un menu "Fichier" contenant l'action "Ouvrir" qui ouvrira un QFileDialog pour retourner le chemin d'accès (path) du fichier à ouvrir
