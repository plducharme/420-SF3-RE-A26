# 2.5 La carte du donjon
donjon = [
    ['.', '.', 'M'],
    ['.', 'T', '.'],
    ['M', '.', '.']
]
monstres = 0
for i in range(len(donjon)):
    for j in range(len(donjon[i])):
        if donjon[i][j] == 'T':
            print(f'Trésor en ({i}, {j})')
        elif donjon[i][j] == 'M':
            monstres += 1
print('Monstres :', monstres)

# Bonus : afficher la carte
for rangee in donjon:
    print(' '.join(rangee))
