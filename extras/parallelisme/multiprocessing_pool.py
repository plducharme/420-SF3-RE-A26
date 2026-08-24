# Si on veut exécuter plusieurs processus en parallèle, on peut utiliser la classe Pool du module multiprocessing.
# Permet d'effectuer des calculs en parallèle en utilisant plusieurs processus qui ne partagent pas de mémoire.

# Exemple d'utilisation de Pool pour calculer la racine carrée de plusieurs nombres en parallèle
from multiprocessing import Pool
import math
import time


# Fonction qui calcule la racine carrée d'un nombre
def racine_carree(nombre: float) -> float:
    return math.sqrt(nombre)


# Sous windows, il faut protéger le code qui exécute les processus avec un bloc if __name__ == "__main__":
if __name__ == "__main__":
    # Créer un Pool avec 4 processus
    debut = time.perf_counter()
    with Pool(4) as pool:

        # Utiliser la méthode map pour appliquer la fonction racine_carree à une liste de nombres
        # Les résultats seront retournés dans l'ordre d'entrée
        # map est bloquant, le programme attend que tous les processus soient terminés
        resultats = pool.map(racine_carree, [1, 4, 9, 16, 25])
        print(resultats)
    fin = time.perf_counter()
    print(f"Temps d'exécution parallèle: {fin - debut} secondes")

    # Si on le fait de façon séquentielle
    debut = time.perf_counter()
    resultats = [racine_carree(nombre) for nombre in [1, 4, 9, 16, 25]]
    print(resultats)
    fin = time.perf_counter()
    print(f"Temps d'exécution séquentiel: {fin - debut} secondes")

# Il est aussi possible d'utiliser des queues et des pipes pour communiquer entre les processus
# Voir la documentation pour plus d'informations
# https://docs.python.org/3/library/multiprocessing.html
# https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues
