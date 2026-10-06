import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# quiver permet de dessiner des vecteurs 3D à partir de leurs composantes (x, y, z)

# Vecteur sur l'axe X
ax.quiver(0, 0, 0, 3, 0, 0, color='r', label='Vecteur X (3,0,0)')
# Vecteur sur l'axe Y
ax.quiver(0, 0, 0, 0, 4, 0, color='g', label='Vecteur Y (0,4,0)')
# Vecteur sur l'axe Z
ax.quiver(0, 0, 0, 0, 0, 5, color='b', label='Vecteur Z (0,0,5)')

# Vecteur résultant (norme)
ax.quiver(0, 0, 0, 3, 4, 5, color='m', label='Norme (3,4,5)')

# Calcul et annotation de la norme
norm = np.linalg.norm([3, 4, 5])
ax.text(3, 4, 5, f'Norme = {norm:.2f}', color='m')

ax.set_xlim([0, 6])
ax.set_ylim([0, 6])
ax.set_zlim([0, 6])
ax.set_xlabel("Axe X")
ax.set_ylabel("Axe Y")
ax.set_zlabel("Axe Z")

plt.title("Représentation 3D de trois vecteurs")
ax.legend()
plt.show()
