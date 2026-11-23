# 4.4 La recette de potion
recette = {'herbe', 'miel', 'cristal', 'eau'}
saisie = input('Ingrédients : ').split(',')
inventaire = {i.strip() for i in saisie}
manquants = recette - inventaire
if not manquants:
    print('Potion prête !')
else:
    print('Il manque :', ', '.join(sorted(manquants)))
print('Inutiles :', ', '.join(sorted(inventaire - recette)))
