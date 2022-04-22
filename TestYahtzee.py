import Yahtzee

class TestClass:

    def test_three_ones_should_return_3(self):
        lancer = [1,1,1,2,5]
        resultat = Yahtzee.Game().lance(lancer,1)
        assert resultat ==3
    def test_four_twos_should_return_8(self):
        lancer = [2,1,2,2,2]
        resultat = Yahtzee.Game().lance(lancer,2)
        assert resultat ==8
    def test_two_threes_should_return_6(self):
        lancer = [3,1,3,2,5]
        resultat = Yahtzee.Game().lance(lancer,3)
        assert resultat ==6
    def test_five_fours_should_return_20(self):
        lancer = [4,4,4,4,4]
        resultat = Yahtzee.Game().lance(lancer,4)
        assert resultat ==20
    def test_two_fives_should_return_10(self):
        lancer = [5,1,1,2,5]
        resultat = Yahtzee.Game().lance(lancer,5)
        assert resultat ==11
    def test_three_sixs_should_return_18(self):
        lancer = [6,6,1,6,5]
        resultat = Yahtzee.Game().lance(lancer,6)
        assert resultat ==18
