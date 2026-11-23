"""Tests d'auto-correction : Python, la quête du grimoire (420-SF1-RE).

Utilisation
-----------
Un exercice dont le fichier n'existe pas encore est simplement ignoré
(SKIP). Si un test échoue, lisez le message : il indique ce qui était
attendu. Votre affichage peut différer légèrement des exemples de
l'énoncé (espaces, majuscules) : les tests vérifient l'essentiel.
"""
import ast
import os
import re
import runpy
import unittest
from io import StringIO
from unittest.mock import patch

DOSSIER = os.path.dirname(os.path.abspath(__file__))


class ExerciceTestCase(unittest.TestCase):
    """Outils communs : simule input() et capture ce que print() affiche."""

    def lancer(self, nom, entrees=(), **patches):
        chemin = os.path.join(DOSSIER, nom)
        if not os.path.exists(chemin):
            self.skipTest(f'{nom} est introuvable (pas encore fait ?)')
        contextes = [
            patch('builtins.input', side_effect=list(entrees)),
            patch('sys.stdout', new_callable=StringIO),
        ]
        contextes += [patch(cible, **options) for cible, options in patches.items()]
        # Les patches sont empilés manuellement pour garder le code lisible.
        sortie = None
        try:
            gestionnaires = [c.__enter__() for c in contextes]
            sortie = gestionnaires[1]
            runpy.run_path(chemin)
        except StopIteration:
            self.fail(f'{nom} demande plus de saisies (input) que prévu dans ce test.')
        finally:
            for c in reversed(contextes):
                c.__exit__(None, None, None)
        return sortie.getvalue()

    def assertContient(self, sortie, attendu, message=''):
        self.assertIn(attendu, sortie, message or f"On attendait de voir « {attendu} » dans l'affichage :\n{sortie}")

    def assertAbsent(self, sortie, interdit, message=''):
        self.assertNotIn(interdit, sortie, message or f"« {interdit} » ne devrait pas apparaître :\n{sortie}")


def ensembles_affiches(texte):
    """Extrait les {...} ou [...] d'un affichage, sous forme d'ensembles."""
    resultat = []
    for morceau in re.findall(r'[\{\[][^\}\]]*[\}\]]', texte):
        try:
            valeur = ast.literal_eval(morceau)
            resultat.append(set(valeur))
        except (ValueError, SyntaxError, TypeError):
            pass
    return resultat


class Partie1(ExerciceTestCase):
    """Les sortilèges de texte (str)."""

    def test_1_1(self):
        self.assertContient(self.lancer('ex_1_1.py', ['abracadabra']), 'arbadacarba')
        self.assertContient(self.lancer('ex_1_1.py', ['python']), 'nohtyp')

    def test_1_2(self):
        for mdp in ['dragon', 'Drag1', 'dragonnnn1', 'Dragonnnn']:
            with self.subTest(mdp=mdp):
                sortie = self.lancer('ex_1_2.py', [mdp]).lower()
                self.assertContient(sortie, 'verrouill')
                self.assertAbsent(sortie, 'ouverte')
        sortie = self.lancer('ex_1_2.py', ['Dragon123']).lower()
        self.assertContient(sortie, 'ouverte')
        self.assertAbsent(sortie, 'verrouill')

    def test_1_3(self):
        sortie = self.lancer('ex_1_3.py', ['le dragon dort'])
        self.assertContient(sortie, 'LE DRAGON DORT')
        self.assertContient(sortie, '4')
        self.assertContient(sortie, 'l* dr*g*n d*rt')

    def test_1_4(self):
        sortie = self.lancer('ex_1_4.py', ['Engage le jeu que je le gagne'])
        self.assertContient(sortie.lower(), 'palindrome magique')
        sortie = self.lancer('ex_1_4.py', ['dragon'])
        self.assertAbsent(sortie.lower(), 'palindrome magique')

    def test_1_5(self):
        self.assertContient(self.lancer('ex_1_5.py', ['Alice', 'Tremblay']), 'Alilay')
        self.assertContient(self.lancer('ex_1_5.py', ['Marie', 'Gagnon']), 'Marnon')


class Partie2(ExerciceTestCase):
    """Le sac à dos de l'aventurier (listes)."""

    def test_2_1(self):
        sortie = self.lancer('ex_2_1.py')
        self.assertContient(sortie, "['bouclier', 'épée', 'potion', 'lanterne']")
        self.assertContient(sortie, '4')

    def test_2_2(self):
        lancers = [3, 6, 1, 6, 2, 5, 4, 6, 1, 3]
        sortie = self.lancer('ex_2_2.py', **{'random.randint': {'side_effect': lancers}})
        self.assertContient(sortie, str(lancers), "La liste des lancers doit être affichée.")
        self.assertContient(sortie, '3.7', 'La moyenne devrait être 3.7.')
        self.assertTrue(re.search(r'\b3\b', sortie.split(str(lancers))[-1]),
                        'Le nombre de 6 (3 fois) devrait être affiché.')

    def test_2_3(self):
        sortie = self.lancer('ex_2_3.py')
        self.assertContient(sortie, '[7, 12, 15, 23, 45, 60, 80]')
        self.assertContient(sortie, '[80, 60, 45]')
        self.assertContient(sortie, '[12, 7, 15]')

    def test_2_4(self):
        sortie = self.lancer('ex_2_4.py')
        ordre = ['Cléo', 'Finn', 'Dax', 'Bram', 'Elia']
        positions = [sortie.find(nom) for nom in ordre]
        self.assertNotIn(-1, positions, f"Chaque joueur éliminé doit être affiché :\n{sortie}")
        self.assertEqual(positions, sorted(positions),
                         f"Ordre d'élimination attendu : {', '.join(ordre)}.\n{sortie}")
        self.assertContient(sortie.lower(), 'survivant')
        self.assertTrue(sortie.rstrip().endswith('Aria'),
                        'Le survivant (Aria) doit être affiché en dernier.')

    def test_2_5(self):
        sortie = self.lancer('ex_2_5.py')
        self.assertContient(sortie, '(1, 1)')
        self.assertTrue(re.search(r'Monstres\D*2', sortie), 'Il devrait y avoir 2 monstres.')


class Partie3(ExerciceTestCase):
    """Le bestiaire et la boutique (dictionnaires)."""

    def test_3_1(self):
        sortie = self.lancer('ex_3_1.py')
        self.assertContient(sortie, '50')
        self.assertContient(sortie, 'fantome')
        self.assertContient(sortie, '100', 'Le dragon devrait avoir 100 points de vie.')
        self.assertAbsent(sortie, 'gobelin', 'Le gobelin devrait être supprimé.')
        self.assertAbsent(sortie, '200', 'Les points du dragon devraient avoir été réduits.')

    def test_3_2(self):
        sortie = self.lancer('ex_3_2.py', ['abracadabra'])
        self.assertContient(sortie, "{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}")
        self.assertTrue(re.search(r'a\W+\(?5', sortie.split('}')[-1]),
                        'La lettre la plus fréquente (a, 5 fois) doit être affichée.')

    def test_3_3(self):
        sortie = self.lancer('ex_3_3.py', ['potion', 'licorne', 'corde', 'fin'])
        self.assertContient(sortie, "Le marchand n'a pas ça")
        self.assertContient(sortie, "['potion', 'corde']")
        self.assertContient(sortie, '35')

    def test_3_3_panier_vide(self):
        sortie = self.lancer('ex_3_3.py', ['fin'])
        self.assertContient(sortie, '[]')
        self.assertContient(sortie, '0')

    def test_3_4(self):
        sortie = self.lancer('ex_3_4.py')
        self.assertContient(sortie, 'Aria')
        self.assertContient(sortie, 'magicienne')
        for valeur in ['6', '11', '8']:
            self.assertContient(sortie, valeur, f'Après la montée de niveau, on attend la valeur {valeur}.')
        self.assertTrue(re.search(r'niveau\W+2', sortie), 'Le niveau 2 doit être affiché.')

    def test_3_5(self):
        sortie = self.lancer('ex_3_5.py', ['mon ami voit la lumière'])
        for inconnu in ['[mon]', '[voit]', '[la]']:
            self.assertContient(sortie, inconnu)
        self.assertContient(sortie, 'mellon')
        self.assertContient(sortie, 'ithil')


class Partie4(ExerciceTestCase):
    """La bibliothèque des sorts (ensembles)."""

    def test_4_1(self):
        sortie = self.lancer('ex_4_1.py')
        self.assertContient(sortie, '4')
        self.assertContient(sortie, "['feu', 'foudre', 'glace', 'vent']")

    def test_4_2(self):
        sortie = self.lancer('ex_4_2.py')
        affiches = ensembles_affiches(sortie)
        attendus = {
            'les deux': {'marais', 'château'},
            'au moins un': {'forêt', 'marais', 'volcan', 'château', 'désert', 'glacier'},
            'seulement Aria': {'forêt', 'volcan'},
            'un seul des deux': {'forêt', 'volcan', 'désert', 'glacier'},
        }
        for nom, attendu in attendus.items():
            with self.subTest(resultat=nom):
                self.assertIn(attendu, affiches,
                              f"Résultat « {nom} » introuvable. Affichez chaque résultat "
                              f"avec print(), sous forme d'ensemble ou de liste.\n{sortie}")

    def test_4_3(self):
        sortie = self.lancer('ex_4_3.py', ['portez ce vieux whisky au juge blond qui fume'])
        self.assertContient(sortie.lower(), 'est un pangramme')
        sortie = self.lancer('ex_4_3.py', ['le dragon dort'])
        self.assertAbsent(sortie.lower(), "c'est un pangramme")
        self.assertContient(sortie, 'b c f h i j k m p q s u v w x y z')

    def test_4_4(self):
        sortie = self.lancer('ex_4_4.py', ['herbe,miel,plume'])
        manquants = sortie.split('Inutiles')[0]
        self.assertContient(manquants, 'cristal')
        self.assertContient(manquants, 'eau')
        self.assertAbsent(sortie.lower(), 'potion prête')
        self.assertContient(sortie.split('nutiles')[-1], 'plume')

    def test_4_4_potion_prete(self):
        sortie = self.lancer('ex_4_4.py', ['eau,cristal,miel,herbe'])
        self.assertContient(sortie.lower(), 'potion prête')


class DefiFinal(ExerciceTestCase):
    """Le grimoire verrouillé."""

    CHOIX = {'random.choice': {'return_value': 'dragon'}}

    def test_victoire(self):
        sortie = self.lancer('defi_final.py', ['monstres'] + list('dragon'), **self.CHOIX)
        self.assertContient(sortie, 'Bravo')

    def test_defaite(self):
        sortie = self.lancer('defi_final.py', ['monstres'] + list('zxwqkj'), **self.CHOIX)
        self.assertContient(sortie.lower(), 'scellé')
        self.assertContient(sortie, 'dragon', 'Le mot secret devrait être révélé à la fin.')

    def test_entrees_invalides_sans_penalite(self):
        entrees = ['monstres', 'ab', '1', ''] + list('dragon')
        sortie = self.lancer('defi_final.py', entrees, **self.CHOIX)
        self.assertContient(sortie, 'Bravo', 'Une entrée invalide ne doit pas coûter d\'essai.')

    def test_lettre_repetee_sans_penalite(self):
        entrees = ['monstres'] + ['z'] * 7 + list('dragon')
        sortie = self.lancer('defi_final.py', entrees, **self.CHOIX)
        self.assertContient(sortie, 'Bravo', 'Une lettre déjà proposée ne doit pas coûter d\'essai.')

    def test_theme_invalide(self):
        entrees = ['cuisine', 'monstres'] + list('dragon')
        sortie = self.lancer('defi_final.py', entrees, **self.CHOIX)
        self.assertContient(sortie, 'Bravo', 'Un thème inconnu doit être redemandé.')


if __name__ == '__main__':
    unittest.main(verbosity=2)