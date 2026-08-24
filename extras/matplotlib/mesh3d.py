import matplotlib.pyplot as plt
from matplotlib import colormaps as cm
import numpy as np

# Créer la figure
fig = plt.figure()

# Créer un axe 3D
ax = fig.add_subplot(111, projection='3d')

# Créer des données
# Utilise np.arange() pour créer un tableau de valeurs
coords_x = np.arange(-10, 10, 0.25)
coords_y = np.arange(-10, 10, 0.25)

# Créer les mailles (mesh) à partir des coordonnées
mesh_x, mesh_y = np.meshgrid(coords_x, coords_y)

# Créer les valeurs de Z à partir des coordonnées X et Y, dans ce cas, Z = sin(sqrt(X^2 + Y^2))
mesh_z = np.sin(np.sqrt(mesh_x ** 2 + mesh_y ** 2))

# On utilise plot_surface() pour afficher la surface
# cmap est un paramètre optionnel pour spécifier le map de couleur (à une valeur, il associe une couleur)
# plusieurs maps de couleur sont disponibles, voir: https://matplotlib.org/stable/tutorials/colors/colormaps.html
surface = ax.plot_surface(mesh_x, mesh_y, mesh_z, cmap=cm["coolwarm"])

# Ajouter une barre de couleur pour indiquer les valeurs (ajout d'un autre axe au graphique)
fig.colorbar(surface)

plt.show()

# Mettre quatre graphiques 3D sur la même figure
# Créer la figure et ses axes
# Le layout permet de spécifier la disposition des axes
# Ceci va créer 4 "axes" (graphiques) sur la figure
# Les positions sont indexées de 0 à 3 (de gauche à droite, de haut en bas; 2*2)
fig, axes = plt.subplots(2, 2, layout="constrained")


# Créer un graphique
def creer_graphique(ax, max_min):
    x = np.linspace(-max_min, max_min, 100)
    y = np.linspace(-max_min, max_min, 100)
    ax.plot(x, y)


# Ajouter le "plot" à chaque axe, dans l'ordre de gauche à droite, de haut en bas
# enumerate permet de boucler sur une liste et de retourner l'index et la valeur
for index, ax in enumerate(axes.flat):
    creer_graphique(ax, 10*index)
plt.show()


# Créer une figure avec des axes à des positions spécifiques
fig = plt.figure()
# equivalent à fig.add_subplot(231)
# 2 lignes, 3 colonnes, position 1
ax1 = fig.add_subplot(2, 3, 1, projection="hammer")
# 2 lignes, 3 colonnes, position 2
fig.add_subplot(232, projection="lambert")
# 2 lignes, 3 colonnes, position 3
fig.add_subplot(233, projection='polar')
# 2 lignes, 3 colonnes, position 4
fig.add_subplot(234, facecolor="pink")
# 2 lignes, 3 colonnes, position 5
fig.add_subplot(235, facecolor="red")

fig.show()
