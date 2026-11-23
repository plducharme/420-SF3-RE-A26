# 2.4 La patate chaude du dragon
joueurs = ['Aria', 'Bram', 'Cléo', 'Dax', 'Elia', 'Finn']
debut = 0
while len(joueurs) > 1:
    i = (debut + 2) % len(joueurs)
    print('Éliminé :', joueurs.pop(i))
    debut = i % len(joueurs)
print('Survivant :', joueurs[0])
