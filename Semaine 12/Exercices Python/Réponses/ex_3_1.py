# 3.1 Le bestiaire
bestiaire = {'gobelin': 10, 'troll': 50, 'dragon': 200}
print(bestiaire['troll'])
bestiaire['fantome'] = 30
bestiaire['dragon'] //= 2
del bestiaire['gobelin']
for monstre, pv in bestiaire.items():
    print(monstre, ':', pv)
