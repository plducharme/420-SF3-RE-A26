import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

# Déclarer un ndarray
array_1d = np.array(np.arange(0, 12, 1), dtype=np.int16)
print(array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d)

array_moy = np.array([75.0, 86.6, 65.2, 45.7, 99.9, 72.4])
print(f"Array pour les calculs:{array_moy}")
# moyenne
print(f"Moyenne:{np.mean(array_moy)}")
# médiane
print(f"Médiane:{np.median(array_moy)}")
# Écart type
print(f"Écart Type:{np.std(array_moy)}")

# exemple arange
array_arange = np.array(np.arange(0.25, 2.76, 0.25))
print(array_arange)

# linespace
array_linspace = np.array(np.linspace(2, 50, 25))
array_x = np.arange(0, 25)
fig = plt.figure()
plt.plot(array_x, array_linspace, marker="o", color="b", linestyle="--")
plt.title("Valeurs générées par linspace()")
plt.grid()
plt.show()






