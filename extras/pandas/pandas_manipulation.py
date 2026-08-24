from pandas import DataFrame
import matplotlib.pyplot as plt

# Initialiser un DataFrame à partir d'un dictionnaire
df = DataFrame({
    "Nom": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Âge": [25, 30, 35, 40, 23],
    "Ville": ["Montréal", "Québec", "Sherbrooke", "Trois-Rivières", "Pembroke"]
})

# Afficher le DataFrame
print(df)

# Ajouter une colonne
df["Province"] = ["Québec", "Québec", "Québec", "Québec", "Ontario"]
print(f"Après ajout colonne\n{df}")

# Supprimer une colonne
# inplace=True permet de modifier le DataFrame original au lieu de retourner un nouveau DataFrame
df.drop(columns=["Province"], inplace=True)
print(df)
# Réajouter la colonne Province
df["Province"] = ["Québec", "Québec", "Québec", "Québec", "Ontario"]
# Retourne une copie du DataFrame sans la colonne Province
df2 = df.drop(columns=["Province"])

# Afficher les 5 premières lignes
print(df.head(5))

# Afficher les 2 dernières lignes
print(df.tail(2))

# Afficher les informations du DataFrame
# Permet entre autres de voir le type de données de chaque colonne
print("info()")
df.info()

# Afficher les statistiques du DataFrame
print("describe()")
print(df.describe())

# Filtrer les données d'une colonne selon une condition
# Remarquez la condition logique df["Âge"] > 30, ceci peut être fait sur n'importe quelle colonne
print("Filtrer les données")
print(df[df["Âge"] > 30])

# Trier les données selon une colonne
print("Trier les données")
print(df.sort_values(by="Âge", ascending=False))

series_ages = df["Âge"]
print(series_ages)
print(type(series_ages))

# Valide si une valeur est dans la série, retourne une série de booléens pour chaque index (ligne de la série)
# True si la valeur est dans la série, False sinon
print("Vérifier si 30 et 35 sont dans la série")
print(series_ages.isin([30, 35]))

# Comme isin() retourne une série de booléens, on peut l'utiliser pour filtrer les données
# Ceci retournera une Series contenant seulement les valeurs de la Series qui sont 30 ou 35
print(series_ages[series_ages.isin([30, 35])])

# Créer un DataFrame à partir d'une liste de listes.
# Il faut spécifier les noms des colonnes en argument
data = [
    ["The Legend of Zelda", "Nintendo EPD", "Nintendo"],
    ["God of War", "Santa Monica Studio", "Sony Interactive Entertainment"],
    ["Halo Infinite", "343 Industries", "Xbox Game Studios"],
    ["Cyberpunk 2077", "CD Projekt Red", "CD Projekt"],
    ["The Witcher 3", "CD Projekt Red", "CD Projekt"]
]

# Initialiser le DataFrame
df_jeux = DataFrame(data, columns=["Jeu", "Studio", "Editeur"])
print(df_jeux)

# Affichage d'un graphique à partir d'un DataFrame avec matplotlib
# voir l'import en haut du fichier
# La figure est un conteneur pour les graphiques
plt.figure(figsize=(10, 5))

plt.plot(df["Nom"], df["Âge"], marker="o", color="red", linestyle="--", label="Âge")
# Titre du graphique
plt.title("Âge des personnes")
# Nom des axes
plt.xlabel("Nom")
plt.ylabel("Âge")
# Afficher la légende
plt.legend()
# Afficher la grille
plt.grid(True)
# Afficher le graphique que l'on vient de configurer
plt.show()

# Grouper les données selon une colonne
# Ici, on groupe les données selon la colonne "Province"
# On compte le nombre de personnes par province
# On utilise la fonction count() pour compter le nombre de lignes par groupe
df_grouped = df.groupby("Province").count()
print(df_grouped)

print("Itérer sur un DataFrame")
# Itérer sur un DataFrame
# iterrows() retourne un itérable sur les lignes du DataFrame
# Chaque ligne est un tuple (index, Series)
for index, ligne in df.iterrows():
    print(f"Index: {index} Ligne: {ligne["Nom"]}, {ligne["Âge"]}, {ligne["Ville"]}, {ligne["Province"]}")
