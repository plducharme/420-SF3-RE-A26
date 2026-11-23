mdp = input('Mot de passe : ')
raisons = []
if len(mdp) < 8:
    raisons.append('trop court')
if mdp.lower() == mdp:
    raisons.append('aucune majuscule')
contient_chiffre = False
for c in mdp:
    if c.isdigit():
        contient_chiffre = True
        break
if not contient_chiffre:
    raisons.append("aucun chiffre")
# if not any(c.isdigit() for c in mdp):
#     raisons.append('aucun chiffre')
if len(raisons) > 0:
    print('Porte verrouillée :', ', '.join(raisons))
else:
    print('Porte ouverte')