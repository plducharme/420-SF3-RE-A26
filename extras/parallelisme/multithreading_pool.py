import threading
import concurrent.futures


def afficher_thread(numero: int):
    print(f"Thread {numero}")


if __name__ == "__main__":
    # Un ThreadPoolExecutor permet d'exécuter des fonctions en parallèle. Un pool de workers (le nombre de threads en
    # parallèle à la fois) est créé. Le pool est fermé automatiquement à la fin du bloc with.
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        # Sera exécuté 25 fois en tout, mais seulement 4 en même temps
        for i in range(25):
            # Techniquement, submit() retourne un objet Future, mais on ne s'en sert pas ici. Submit() sert à céduler
            # une fonction à exécuter dans le ThreadPoolExecutor.
            executor.submit(afficher_thread, i)
