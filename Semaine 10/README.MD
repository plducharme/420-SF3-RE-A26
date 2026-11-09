# Application d'affichage de la qualité de l'air
1) Complétez ``generateur_csv`` pour créer un csv ``airdata-{date}.csv`` et générer pour 3 dates (288 enregistrements par date)
2) Utilisez PyCharm pour créer une BD sqlite et importer le data des csv
   - Utilisez la vue Database de PyCharm pour créer et importer
3) Créez un module sqlalchemy correspondant pour intéragir à la BD sqlite
   - Alternativement, utiliser Pandas pour se connecter à la BD et aller chercher tous les enregistrements 
4) Créer une application PySide6
   - Un menu ``Fichier``
     - Exporter graphique en PDF
     - Quitter
   - Une barre d'outils contenant les actions
   - L'application devra utiliser l'ORM pour intéragir avec la BD
   - Une interface contenant
     - un ``QCalendarWidget`` permettant de choisir une journée
       - utiliser ``setDateRange()`` ou ``minimumDate`` et ``maximumDate`` 
     - un ``QComboBox`` qui contiendra les ``datetime`` des enregistrements de la journée sélectionnée avec le QCalendarWidget
     - Une interface au choix permettant d'afficher les informations du ``datetime`` sélectionné
     - Un graphique ``matplotlib`` qui affichera les données ``pm25`` pour la journée choisie
     - Donnez un titre et une icône cool à votre application