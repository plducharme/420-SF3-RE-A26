# 1.5 Ton nom de dragon
import random
prenom = input('Prénom : ')
nom = input('Nom : ')
dragon = prenom[0:3]
dragon += nom[-3:]
dragon = dragon.capitalize()
titres = ["le Redoutable", "le Badass", "Le Magnifique"]
print(f'Ton nom de dragon : {dragon} {random.choice(titres)}')
