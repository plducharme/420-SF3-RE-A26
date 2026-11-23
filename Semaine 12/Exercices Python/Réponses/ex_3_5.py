# 3.5 Le traducteur elfique
elfique = {
    'ami': 'mellon', 'lumière': 'ithil', 'étoile': 'elen',
    'eau': 'nen', 'arbre': 'galadh', 'ciel': 'menel'
}
mots = input('Phrase : ').split()
traduits = [elfique.get(m, f'[{m}]') for m in mots]
print(' '.join(traduits))
