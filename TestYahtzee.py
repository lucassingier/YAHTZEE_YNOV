import Yahtzee
from unittest import TestCase, mock, main

class TestClass(TestCase):

    def test_three_ones_should_return_3(self):
        lancer = [1,1,1,2,5]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="Ones":
                self.assertEqual(3,valeur)
                
    def test_four_twos_should_return_8(self):
        lancer = [2,1,2,2,2]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="Twos":
                self.assertEqual(8,valeur)

    def test_two_threes_should_return_6(self):
        lancer = [3,1,3,2,5]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="Threes":
                self.assertEqual(6,valeur)

    def test_five_fours_should_return_20(self):
        lancer = [4,4,4,4,4]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="Fours":
                self.assertEqual(20,valeur)

    def test_two_fives_should_return_10(self):
        lancer = [5,1,1,2,5]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="Fives":
                self.assertEqual(10,valeur)

    def test_three_sixs_should_return_18(self):
        lancer = [6,6,1,6,5]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="Sixes":
                self.assertEqual(18,valeur)

if __name__ == '__main__':
  main()