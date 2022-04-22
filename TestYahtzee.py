import Yahtzee

class TestClass:

    def test_three_ones_should_return_3(self):
        lancer = [1,1,1,2,5]
        resultat = Yahtzee.Game().lance(lancer)
        assert resultat ==3
