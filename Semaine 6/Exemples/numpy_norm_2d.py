import matplotlib.pyplot as plt
import numpy as np

# Créer une figure et un axe
fig, ax = plt.subplots()

# Dessiner les vecteurs à partir de l'origine (0,0)
ax.quiver(0, 0, 3, 0, label='Vecteur X (3,0)', color='r', angles='xy', scale_units='xy', scale=1)
ax.quiver(0, 0, 0, 4, label='Vecteur Y (0,4)', color='g', angles='xy', scale_units='xy', scale=1)

# Dessiner le vecteur résultant (norme)
# En 2D, la norme est l'hypoténuse
norm = np.linalg.norm([3, 4])
ax.quiver(0, 0, 3, 4, label=f"Norme (3,4) = {norm:.2f}", color='b', angles='xy', scale_units='xy', scale=1)

ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

plt.legend()
plt.show()

# Autre façon de dessiner les vecteurs
norm_2 = np.linalg.norm([4, 5])
plt.figure()
plt.plot([1, 4], [1, 1], 'r-', label='Vecteur X (4,1)')
plt.plot([1, 1], [1, 5], 'g-', label='Vecteur Y (1,5)')
plt.plot([1, 4], [1, 5], 'b-', label=f'Norme (4,5) = {norm_2:.2f}')
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.legend()
plt.grid()
plt.show()

