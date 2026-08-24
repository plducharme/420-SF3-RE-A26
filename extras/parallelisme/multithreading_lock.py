# Un des problèmes de la programmation concurrente est la concurrence pour les ressources partagées.
# Si deux threads tentent de modifier une même variable en même temps, il peut y avoir des problèmes. Par exemple, si un
# thread lit la valeur d'une variable, puis un autre thread la modifie, le premier thread peut utiliser une valeur
# obsolète.
# Pour éviter cela, on peut utiliser un verrou (lock) pour bloquer l'accès à la ressource partagée pendant qu'un thread
# l'utilise.

import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor


class Compteur:
    def __init__(self):
        self.valeur = 0
        # Créer un verrou
        self.lock = threading.Lock()

    def incrementer(self, locked=True):
        # On bloque l'accès à la ressource partagée
        # Si un thread a déjà le verrou, les autres threads attendent
        # On peut utiliser un block with pour s'assurer que le verrou est relâché même si une exception est levée.
        # Alternativement, on peut appeler acquire() et release() manuellement.
        if locked:
            with self.lock:
                copie_locale = self.valeur
                copie_locale += 1
                time.sleep(0.1)
                self.valeur = copie_locale
        else:
            copie_locale = self.valeur
            copie_locale += 1
            time.sleep(0.1)
            self.valeur = copie_locale

        print(threading.current_thread().name, self.valeur, locked)


if __name__ == "__main__":
    compteur_locked = Compteur()


    def incrementer_compteur(compteur: Compteur, locked=True):
        for _ in range(10):
            compteur.incrementer(locked)


    with ThreadPoolExecutor(max_workers=8) as executor:
        for _ in range(10):
            executor.submit(incrementer_compteur, compteur_locked, True)

    compteur_unlocked = Compteur()

    with ThreadPoolExecutor(max_workers=8) as executor:
        for _ in range(10):
            executor.submit(incrementer_compteur, compteur_unlocked, False)

    print("Avec le verrou", compteur_locked.valeur)
    print("Sans le verrou", compteur_unlocked.valeur)
    print("Résultat attendu: 100")
