import pandas as pd


class Impex:
    def __init__(self):
        # Import à partir d'un fichier CSV
        # De façon similaire, il existe des read_json, read_excel, read_sql, etc.
        # On obtient un objet DataFrame (représentation tabulaire des données (dictionnaire))
        # Les clés sont les noms des colonnes et les valeurs sont des objets Series
        print("Import du csv")
        self.df = pd.read_csv('Water-Qual-Eau-Sites-National.csv', sep=',')
        # Impression des dix premières lignes
        print(self.df.head(10))
        # Impression des dix dernières lignes
        print(self.df.tail(10))
        # Impression des colonnes
        print(self.df.columns)
        # Impression d'une colonne
        print(self.df['SITE_NAME'])

        # Export vers un fichier excel (nécessite package openpyxl)
        self.df.to_excel('./output/Water-Qual-Eau-Sites-National.xlsx', index=False)
        # Export vers un fichier json
        self.df.to_json('./output/Water-Qual-Eau-Sites-National.json', orient='records')
        # D'autres exportations sont possibles (to_sql, to_html, to_latex, etc.)

        # information sommaire sur le DataFrame (compte, moyenne, écart-type, minimum, maximum, percentiles, max)
        print(self.df.describe())


impex = Impex()
