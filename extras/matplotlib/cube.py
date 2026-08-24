import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Dessiner des faces de polygones en utilisant matplotlib

# Les coordonnées des sommets des faces: tuple (x, y, z)
sommets = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (1, 1, 1), (0, 1, 1), (0, 0, 1), (1, 0, 1)]

# Les faces sont des listes de sommets
# Chaque sommet est un tuple (x, y, z), on relie les sommets dans l'ordre pour former une face (donc 4 sommets par face)
faces = [[sommets[0], sommets[1], sommets[2], sommets[3]],
         [sommets[1], sommets[0], sommets[6], sommets[7]],
         [sommets[7], sommets[6], sommets[5], sommets[4]],
         [sommets[4], sommets[5], sommets[3], sommets[2]],
         [sommets[2], sommets[1], sommets[7], sommets[4]],
         [sommets[5], sommets[6], sommets[0], sommets[3]]]

# Les couleurs des faces, pour mieux les distinguer
couleurs = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# Créer une figure
fig = plt.figure()

# Créer un axe 3D
ax = fig.add_subplot(111, projection='3d')
# Pour chaque face, on dessine un polygone
for i in range(6):
    ax.add_collection3d(Poly3DCollection([faces[i]], facecolors=couleurs[i], linewidths=1, edgecolors='r'))

# Afficher les sommets (ajout de points noirs aux sommets)
ax.scatter([s[0] for s in sommets], [s[1] for s in sommets], [s[2] for s in sommets], color='black')
# Afficher le graphique
fig.show()
