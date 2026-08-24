import matplotlib.pyplot as plt
import numpy as np

# Créer un graphique à partir de données
# On peut utiliser une liste ou un array de numpy
valeurs_x = np.array([1.0, 2.5, 3.5, 4.7, 5.9, 6.0])
valeurs_y = np.array([4.6, 1.2, 2.4, 3.5, 1.0, 4.0])

# Graphique à points reliant les points par une ligne
plt.plot(valeurs_x, valeurs_y)
plt.show()

# Graphique à point (Scatter plot)
plt.scatter(valeurs_x, valeurs_y)
plt.show()

# Graphique à barres
plt.bar(valeurs_x, valeurs_y)
plt.show()

# Graphique à barres horizontales
plt.barh(valeurs_x, valeurs_y)
plt.show()

# Afficher plusieurs graphiques sur la même figure
# Créer une nouvelle figure
plt.figure()
# Pour travailler sur les graphiques de la même figure, on utilise subplot
# Le premier chiffre est le nombre de lignes, le deuxième le nombre de colonnes et le troisième la position du subplot
plt.subplot(111)
plt.plot(valeurs_x, valeurs_y)
plt.subplot(111)
plt.scatter(valeurs_x, valeurs_y)
plt.subplot(111)
plt.title("Barres")
plt.bar(valeurs_x, valeurs_y)
plt.show()

# Projection 3D
valeurs_z = np.array([1.0, 4.2, 3.7, 6.7, 2.9, 6.0])
fig = plt.figure()
# On ajoute un subplot en 3D
ax = fig.add_subplot(111, projection="3d")
ax.scatter(valeurs_x, valeurs_y, valeurs_z, marker="o", color="blue")
plt.show()

# Annoter un graphique
# Générer les valeurs en x entre 0 et 5 avec un pas de 0.01
cosinus_x = np.arange(0.0, 5.0, 0.01)
# Calculer le cosinus de chaque valeur en x
cosinus_y = np.cos(2 * np.pi * cosinus_x)
# Créer un graphique
plt.plot(cosinus_x, cosinus_y)
# Ajouter une annotation
# xy : position de l'annotation
# xytext : position du texte de l'annotation
# arrowprops : propriétés de la flèche
plt.annotate("Maximum local", xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor="black", shrink=0.05))
plt.ylim(-2, 2)
plt.show()
