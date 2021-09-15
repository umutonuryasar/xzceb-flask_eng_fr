import unittest

from translator import english_to_french
from translator import french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french(0), '0')  # test when 0 is given as input the output is 0.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when Hello is given as input the output is Bonjour.
        self.assertEqual(english_to_french('Yes'), 'Oui')  # test when Yes is given as input the output is Oui.
        self.assertEqual(english_to_french('Color'), 'Couleur')  # test when Color is given as input the output is Couleur.


class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english(0), '0')  # test when 0 is given as input the output is 0.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when Bonjour is given as input the output is Hello.
        self.assertEqual(french_to_english('Oui'), 'Yes')  # test when Oui is given as input the output is Yes.
        self.assertEqual(french_to_english('Couleur'), 'Color')  # test when Couleur is given as input the output is Color.


unittest.main()
