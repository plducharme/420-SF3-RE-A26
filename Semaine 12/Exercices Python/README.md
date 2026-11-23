# Python : la quête du grimoire (420-SF1-RE)

## Bienvenue, apprenti sorcier

Vous venez d'hériter de la tour du vieux sorcier Pythonius, mais son grimoire est verrouillé : seul un programmeur capable de manipuler les chaînes de caractères, les listes, les dictionnaires et les ensembles saura le rouvrir.

Ce document contient 19 exercices répartis en quatre parties, suivis d'un défi final qui réunit toutes les notions. Chaque exercice porte une difficulté de ★ (facile) à ★★★ (costaud).

### Consignes

1. Créez un fichier `.py` par exercice, nommé selon son numéro (par exemple `ex_1_3.py`).
2. Utilisez `input()` et `print()` pour interagir avec l'utilisateur, sauf si l'énoncé précise autre chose.
3. Testez votre programme avec les exemples fournis, puis avec vos propres valeurs.
4. Aucun module externe n'est requis, sauf `random` et `string` lorsque l'énoncé les mentionne.
5. Ajoutez un commentaire d'une ligne au-dessus de chaque bloc pour expliquer ce qu'il fait.

**Matériel suggéré :** les méthodes `upper()`, `split()`, `join()`, `append()`, `items()`, `get()` et les opérateurs d'ensembles (`&`, `|`, `-`, `^`) sont à votre disposition.

---

## Partie 1 : les sortilèges de texte (str)

### Exercice 1.1 — Le sort inversé (★)

Le sorcier ne comprend que les incantations lues à l'envers. Demandez un mot à l'utilisateur et affichez-le inversé, sans utiliser de boucle.

```text
Mot : abracadabra
Sort inversé : arbadacarba
```

*Indice : le découpage (slicing) accepte un pas négatif.*

### Exercice 1.2 — Le mot de passe du donjon (★★)

La porte du donjon n'accepte qu'un mot de passe valide : au moins 8 caractères, au moins une majuscule et au moins un chiffre. Demandez un mot de passe et affichez `Porte ouverte` ou `Porte verrouillée` avec la ou les raisons du refus.

```text
Mot de passe : dragon
Porte verrouillée : trop court, aucune majuscule, aucun chiffre
```

### Exercice 1.3 — Le chuchoteur de voyelles (★)

Un message secret doit être crypté avant de traverser la forêt. Pour une phrase saisie par l'utilisateur, affichez : (a) la phrase en majuscules, (b) le nombre de voyelles, (c) la phrase où chaque voyelle est remplacée par `*`.

```text
Phrase : le dragon dort
LE DRAGON DORT
Voyelles : 4
l* dr*g*n d*rt
```

### Exercice 1.4 — Le palindrome magique (★★)

Certaines phrases se lisent dans les deux sens et déjouent les maléfices. Écrivez un programme qui détermine si une phrase est un palindrome, en ignorant les espaces et la casse.

```text
Phrase : Engage le jeu que je le gagne
Palindrome magique !
```

### Exercice 1.5 — Ton nom de dragon (★★)

À partir du prénom et du nom de famille de l'utilisateur, générez son nom de dragon : les trois premières lettres du prénom suivies des trois dernières lettres du nom, avec une majuscule initiale, puis un titre de votre choix. Utilisez une f-string pour l'affichage.

```text
Prénom : Alice
Nom : Tremblay
Ton nom de dragon : Alilay le Redoutable
```

---

## Partie 2 : le sac à dos de l'aventurier (listes)

### Exercice 2.1 — L'inventaire (★)

Votre sac à dos contient au départ `['épée', 'potion', 'corde']`. Dans l'ordre : ajoutez une `lanterne` à la fin, insérez un `bouclier` en première position, retirez la `corde`, puis affichez le contenu du sac et le nombre d'objets.

```text
['bouclier', 'épée', 'potion', 'lanterne']
Objets : 4
```

### Exercice 2.2 — Le dé du destin (★★)

Simulez 10 lancers d'un dé à 6 faces avec `random.randint(1, 6)` et rangez les résultats dans une liste. Affichez la liste, la plus grande valeur, la plus petite, la moyenne et le nombre de fois où le dé a donné 6.

```text
Lancers : [3, 6, 1, 6, 2, 5, 4, 6, 1, 3]
Max : 6   Min : 1   Moyenne : 3.7   Nombre de 6 : 3
```

### Exercice 2.3 — Le marchand de potions (★★)

Voici les prix de potions : `[45, 12, 80, 7, 23, 60, 15]`. Affichez (a) la liste triée du moins cher au plus cher sans modifier la liste d'origine, (b) les trois potions les plus chères, (c) la liste des potions qui coûtent moins de 20 pièces d'or.

```text
Triée : [7, 12, 15, 23, 45, 60, 80]
Top 3 : [80, 60, 45]
Abordables : [12, 7, 15]
```

*Bonus : écrivez (c) en une seule ligne avec une compréhension de liste.*

### Exercice 2.4 — La patate chaude du dragon (★★★)

Six aventuriers sont en cercle : `['Aria', 'Bram', 'Cléo', 'Dax', 'Elia', 'Finn']`. Le dragon élimine un joueur à chaque ronde en comptant de 3 en 3 à partir du premier, et le cercle se referme. Affichez qui est éliminé à chaque ronde et qui survit.

```text
Éliminé : Cléo
Éliminé : Finn
Éliminé : Dax
Éliminé : Bram
Éliminé : Elia
Survivant : Aria
```

*Indice : `pop(index)` retire un élément, et l'opérateur `%` permet de « faire le tour ».*

### Exercice 2.5 — La carte du donjon (★★★)

Le donjon est une grille représentée par une liste de listes :

```python
donjon = [
    ['.', '.', 'M'],
    ['.', 'T', '.'],
    ['M', '.', '.']
]
```

`M` représente un monstre, `T` le trésor et `.` une case vide. Parcourez la grille avec deux boucles imbriquées, affichez les coordonnées (ligne, colonne) du trésor, puis le nombre total de monstres.

```text
Trésor en (1, 1)
Monstres : 2
```

*Bonus : affichez la carte avec une ligne de texte par rangée de la grille.*

---

## Partie 3 : le bestiaire et la boutique (dictionnaires)

### Exercice 3.1 — Le bestiaire (★)

Créez le dictionnaire `bestiaire = {'gobelin': 10, 'troll': 50, 'dragon': 200}` où chaque clé est un monstre et chaque valeur ses points de vie. Dans l'ordre : affichez les points de vie du troll, ajoutez un `fantome` à 30 points, réduisez de moitié ceux du dragon (division entière), supprimez le gobelin, puis affichez chaque monstre avec ses points de vie en utilisant `items()`.

```text
50
troll : 50
dragon : 100
fantome : 30
```

### Exercice 3.2 — Le compteur de lettres (★★)

Le sorcier veut savoir quelles lettres reviennent le plus souvent dans une incantation. Pour une phrase saisie, construisez un dictionnaire qui associe chaque lettre (sans les espaces) à son nombre d'apparitions, puis affichez la lettre la plus fréquente.

```text
Phrase : abracadabra
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
Lettre la plus fréquente : a (5 fois)
```

*Indice : `get(lettre, 0)` évite de tester si la clé existe déjà.*

### Exercice 3.3 — La boutique du marchand (★★)

Le marchand vend les articles suivants :

```python
boutique = {'épée': 150, 'potion': 25, 'bouclier': 90, 'corde': 10}
```

Demandez à l'utilisateur d'entrer des articles un par un, jusqu'à ce qu'il tape `fin`. Si l'article existe, ajoutez-le au panier (une liste). Sinon, affichez `Le marchand n'a pas ça !`. À la fin, affichez le panier et le total à payer.

```text
Article : potion
Article : licorne
Le marchand n'a pas ça !
Article : corde
Article : fin
Panier : ['potion', 'corde']   Total : 35 pièces d'or
```

### Exercice 3.4 — La fiche de personnage (★★)

Un dictionnaire peut contenir d'autres dictionnaires :

```python
heros = {
    'nom': 'Aria',
    'classe': 'magicienne',
    'niveau': 1,
    'stats': {'force': 4, 'magie': 9, 'agilité': 6}
}
```

Écrivez une première partie qui affiche la fiche de façon lisible, puis une seconde partie qui simule une montée de niveau : le niveau augmente de 1 et chaque statistique augmente de 2. Affichez la fiche à nouveau.

```text
Aria, magicienne (niveau 2)
  force : 6
  magie : 11
  agilité : 8
```

### Exercice 3.5 — Le traducteur elfique (★★★)

Créez un petit dictionnaire français → elfique d'au moins 6 mots (par exemple `'ami': 'mellon'`, `'lumière': 'ithil'`). Demandez une phrase en français, traduisez-la mot à mot, et conservez entre crochets les mots absents du dictionnaire.

```text
Phrase : mon ami voit la lumière
[mon] mellon [voit] [la] ithil
```

*Indice : `split()` découpe la phrase, `join()` la reconstruit.*

---

## Partie 4 : la bibliothèque des sorts (ensembles)

### Exercice 4.1 — Les doublons du grimoire (★)

Le grimoire contient des sorts copiés plusieurs fois :

```python
sorts = ['feu', 'glace', 'feu', 'foudre', 'glace', 'feu', 'vent']
```

Convertissez la liste en ensemble pour éliminer les doublons, affichez le nombre de sorts différents, puis affichez les sorts en ordre alphabétique.

```text
Sorts différents : 4
['feu', 'foudre', 'glace', 'vent']
```

*Indice : un ensemble n'a pas d'ordre, mais `sorted()` retourne une liste triée.*

### Exercice 4.2 — Les quêtes en commun (★★)

Deux héros ont terminé des quêtes différentes :

```python
aria = {'forêt', 'marais', 'volcan', 'château'}
bram = {'marais', 'château', 'désert', 'glacier'}
```

À l'aide des opérateurs d'ensembles, affichez : (a) les quêtes terminées par les deux, (b) toutes les quêtes terminées par au moins un des deux, (c) les quêtes que seule Aria a terminées, (d) les quêtes terminées par un seul des deux héros.

*Les ensembles n'étant pas ordonnés, l'ordre d'affichage peut varier d'une exécution à l'autre.*

### Exercice 4.3 — Le détective des pangrammes (★★)

Un pangramme est une phrase qui contient toutes les lettres de l'alphabet. Demandez une phrase à l'utilisateur et déterminez s'il s'agit d'un pangramme. Sinon, affichez les lettres manquantes en ordre alphabétique.

```text
Phrase : portez ce vieux whisky au juge blond qui fume
C'est un pangramme !

Phrase : le dragon dort
Pas un pangramme. Lettres manquantes : b c f h i j k m p q s u v w x y z
```

*Indice : `import string` donne accès à `string.ascii_lowercase`, qui contient les 26 lettres.*

### Exercice 4.4 — La recette de potion (★★)

Une potion de guérison demande les ingrédients `{'herbe', 'miel', 'cristal', 'eau'}`. Demandez à l'utilisateur de saisir ses ingrédients, séparés par des virgules. Affichez `Potion prête !` s'il les possède tous, sinon affichez la liste des ingrédients manquants. Affichez aussi ses ingrédients inutiles pour cette recette.

```text
Ingrédients : herbe,miel,plume
Il manque : cristal, eau
Inutiles : plume
```

*Indice : cherchez les méthodes `issubset()` ou l'opérateur `<=`, ainsi que la différence d'ensembles.*

---

## Défi final : le grimoire verrouillé (★★★)

Pour ouvrir le grimoire, il faut deviner le mot de passe magique, lettre par lettre, comme au jeu du pendu. Chaque notion du cours y trouve sa place :

| Élément du jeu | Structure à utiliser |
| --- | --- |
| Le mot secret et son affichage (`_ a _ _`) | `str` |
| Les mots disponibles pour chaque thème | `dict` dont les valeurs sont des `list` |
| Les lettres déjà proposées (bonnes et mauvaises) | `set` |
| Les lettres du mot encore à découvrir | `set` |

### Déroulement du jeu

1. Créez un dictionnaire de thèmes, par exemple `{'monstres': ['gobelin', 'dragon', 'fantome'], 'objets': ['bouclier', 'lanterne', 'potion'], 'lieux': ['donjon', 'marais', 'volcan']}`.
2. Affichez les thèmes, laissez l'utilisateur en choisir un, puis choisissez un mot au hasard dans la liste correspondante avec `random.choice()`.
3. À chaque tour, affichez le mot avec les lettres trouvées et des `_` pour les autres, ainsi que les lettres déjà essayées et le nombre d'essais restants (6 au départ).
4. Demandez une lettre. Refusez sans pénalité une entrée invalide (plus d'un caractère ou autre chose qu'une lettre) ou une lettre déjà proposée.
5. Si la lettre est dans le mot, elle est révélée. Sinon, l'utilisateur perd un essai.
6. La partie se termine quand toutes les lettres sont trouvées (le grimoire s'ouvre) ou quand il ne reste plus d'essais (le grimoire reste scellé).

```text
Thème : monstres
_ _ _ _ _ _     Essayées : set()     Essais : 6
Lettre : o
_ _ _ _ o _     Essayées : {'o'}     Essais : 6
Lettre : z
_ _ _ _ o _     Essayées : {'o', 'z'}     Essais : 5
```

**Pour aller plus loin :** ajoutez un système de points (un dictionnaire qui associe chaque thème à son meilleur score), affichez la liste des lettres ratées en ordre alphabétique, ou permettez de rejouer sans quitter le programme.
