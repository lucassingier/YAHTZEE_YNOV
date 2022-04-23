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

    def test_three_of_a_kind_should_return_21(self):
        lancer = [6,6,1,6,2]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="ThreeOfAKind":
                self.assertEqual(21,valeur)

    def test_three_of_a_kind_should_return_29(self):
        lancer = [6,6,6,6,5]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="FourOfAKind":
                self.assertEqual(29,valeur)
    
    def test_full_house_should_return_25(self):
        lancer = [6,6,6,5,5]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="FullHouse":
                self.assertEqual(25,valeur)

    def test_small_straight_should_return_30(self):
        lancer = [1,2,3,4,3]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="SmallStraight":
                self.assertEqual(30,valeur)

    def test_large_straight_should_return_40(self):
        lancer = [1,2,3,4,5]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="LargeStraight":
                self.assertEqual(40,valeur)

    def test_chance_should_return_24(self):
        lancer = [6,4,6,3,5]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="Chance":
                self.assertEqual(24,valeur)

    def test_yahtzee_should_return_50(self):
        lancer = [6,6,6,6,6]
        resultat = Yahtzee.Game().lance(lancer)
        for cle, valeur in resultat.items():
            if cle =="Yahtzee":
                self.assertEqual(50,valeur)
                
if __name__ == '__main__':
  main()
