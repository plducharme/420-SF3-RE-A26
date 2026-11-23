# Défi final : le grimoire verrouillé
import random

themes = {
    'monstres': ['gobelin', 'dragon', 'fantome'],
    'objets': ['bouclier', 'lanterne', 'potion'],
    'lieux': ['donjon', 'marais', 'volcan']
}
print('Thèmes :', ', '.join(themes))
theme = input('Thème : ')
while theme not in themes:
    theme = input('Thème inconnu, réessaie : ')

mot = random.choice(themes[theme])
a_trouver = set(mot)
essayees = set()
essais = 6

while a_trouver and essais > 0:
    affichage = ' '.join(c if c in essayees else '_' for c in mot)
    print(f'{affichage}     Essayées : {essayees}     Essais : {essais}')
    lettre = input('Lettre : ').lower()
    if len(lettre) != 1 or not lettre.isalpha() or lettre in essayees:
        print('Entrée invalide ou lettre déjà essayée.')
        continue
    essayees.add(lettre)
    if lettre in a_trouver:
        a_trouver.remove(lettre)
    else:
        essais -= 1

if not a_trouver:
    print(f"Bravo ! Le grimoire s'ouvre : {mot}")
else:
    print(f'Le grimoire reste scellé. Le mot était : {mot}')
