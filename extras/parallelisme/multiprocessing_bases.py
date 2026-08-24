# Le multiprocessing est une technique de programmation qui permet d'exécuter plusieurs processus en parallèle.
# Ces processus doivent être indépendants les uns des autres et ne pas partager de données.
# À ne pas confondre avec le multithreading qui permet d'exécuter plusieurs threads en parallèle dans un même processus.

# Le module multiprocessing de Python permet de créer des processus en parallèle.
# Il est possible de créer un processus en utilisant la classe Process du module multiprocessing.

# Exemple de base
from multiprocessing import Process
import os


def afficher_pid():
    print(f"Le PID du processus est {os.getpid()}")
    print(f"Le PID du processus parent est {os.getppid()}")


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


# Sous Windows, il est nécessaire de protéger le code qui crée des processus avec un bloc if __name__ == "__main__":.
if __name__ == "__main__":
    processus = Process(target=afficher_pid)
    # Démarrer le processus
    processus.start()
    # Attendre que le processus termine
    processus.join()
    # Créer un processus pour trier un tableau, le tableau est passé en argument
    p = Process(target=bubble_sort, args=([64, 34, 25, 12, 22, 11, 90],))
    # Démarrer le processus
    p.start()
    # Attendre que le processus termine
    p.join()

