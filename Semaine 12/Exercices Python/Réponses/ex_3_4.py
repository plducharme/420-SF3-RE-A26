# 3.4 La fiche de personnage
heros = {
    'nom': 'Aria',
    'classe': 'magicienne',
    'niveau': 1,
    'stats': {'force': 4, 'magie': 9, 'agilité': 6}
}


def afficher(h):
    print(f"{h['nom']}, {h['classe']} (niveau {h['niveau']})")
    for stat, valeur in h['stats'].items():
        print(f'  {stat} : {valeur}')


afficher(heros)
heros['niveau'] += 1
for stat in heros['stats']:
    heros['stats'][stat] += 2
print()
afficher(heros)
