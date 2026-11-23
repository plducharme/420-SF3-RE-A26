# 1.3 Le chuchoteur de voyelles
phrase = input('Phrase : ')
voyelles = 'aeiouy'
print(phrase.upper())
nb_voyelles = 0
for c in phrase.lower():
    if c in voyelles:
        nb_voyelles += 1
print(f"Voyelles : {nb_voyelles}")
resultat = ''
for c in phrase:
    if c.lower() in voyelles:
        resultat += "*"
    else:
        resultat += c
# Autre méthode
# res2 = phrase
# for v in voyelles:
#     res2 = res2.replace(v, "*")
# print(res2)
print(resultat)
