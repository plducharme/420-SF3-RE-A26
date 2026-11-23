# 2.3 Le marchand de potions
prix = [45, 12, 80, 7, 23, 60, 15]
print('Triée :', sorted(prix))
print('Top 3 :', sorted(prix, reverse=True)[:3])
abordables = []
for p in prix:
    if p < 20:
        abordables.append(p)
print('Abordables :', abordables)
