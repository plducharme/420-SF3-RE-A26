# Pratique du MVC

## Application de gestion de données sur les sorties de jeux vidéo
Créer une application en respectant l'Architecture MVC

1) Vous devrez avoir une classe qui gère le modèle
   1) Lecture du fichier CSV
   2) Modification du CSV
   3) Calcul des statistiques de plateformes (windows, macos, linux)
2) Vue
   1) Vous devrez construire une vue qui vous permettra d'afficher les données pour une ligne
   2) Capacité à naviguer entre les diverses lignes de données
   3) Possibilité de changer les données et d'appliquer les changements
   4) Devra appeler le contrôleur pour interagir avec le modèle
   5) Devra afficher les statistiques (non-éditable) de l'utilisation des plateformes
3) Contrôleur
   1) À créer dans une classe séparée
   2) La vue initialisera le contrôleur
   3) Le contrôleur appellera les fonctions du modèle
   4) Initialisera le modèle