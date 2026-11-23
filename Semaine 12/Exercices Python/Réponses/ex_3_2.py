# 3.2 Le compteur de lettres
phrase = input('Phrase : ').replace(' ', '')
compte = {}
for lettre in phrase:
    compte[lettre] = compte.get(lettre, 0) + 1
print(compte)
meilleure = max(compte, key=compte.get)
print(f'Lettre la plus fréquente : {meilleure} ({compte[meilleure]} fois)')
