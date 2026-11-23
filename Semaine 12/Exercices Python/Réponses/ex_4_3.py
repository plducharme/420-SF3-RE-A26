# 4.3 Le détective des pangrammes
import string

phrase = input('Phrase : ').lower()
alphabet = set(string.ascii_lowercase)
manquantes = alphabet - set(phrase)
if not manquantes:
    print("C'est un pangramme !")
else:
    print('Pas un pangramme. Lettres manquantes :', ' '.join(sorted(manquantes)))
