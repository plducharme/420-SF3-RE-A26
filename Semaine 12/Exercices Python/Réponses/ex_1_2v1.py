# 1.2 Le mot de passe du donjon
mdp = input('Mot de passe : ')
raisons = []
if len(mdp) < 8:
    raisons.append('trop court')
if mdp.lower() == mdp:
    raisons.append('aucune majuscule')
if not any(c.isdigit() for c in mdp):
    raisons.append('aucun chiffre')
if raisons:
    print('Porte verrouillée :', ', '.join(raisons))
else:
    print('Porte ouverte')
