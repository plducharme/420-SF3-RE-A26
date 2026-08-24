# Un processus est un programme ou une application indépendante qui s'exécute dans son propre espace d'adressage,
# tandis qu'un thread est une unité d'exécution au sein d'un processus qui partage le même espace d'adressage que le
# processus.

import threading


def afficher_n_fois(texte: str, nb_fois: int = 5):
    for i in range(nb_fois):
        print(threading.current_thread().name, texte)


if __name__ == "__main__":
    # Créer des threads
    thread = threading.Thread(target=afficher_n_fois, args=("Bonjour", 25), )
    thread2 = threading.Thread(target=afficher_n_fois, kwargs={"texte": "Salut", "nb_fois": 25})
    # Démarrer les threads
    thread.start()
    thread2.start()
    # Attendre que les threads se terminent
    thread.join()
    thread2.join()
    print("Fin du programme")


