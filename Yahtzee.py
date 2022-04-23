class Game:
    diccombo = {
        "Ones": 1, 
        "Twos": 2,
        "Threes": 3, 
        "Fours": 4, 
        "Fives": 5, 
        "Sixes": 6,
        "ThreeOfAKind": 0,
        "FourOfAKind": 0,
        "FullHouse":0,
        "Chance":0}
    
    def lance(self,lancer):
        resultats ={
        "Ones": 0, 
        "Twos": 0,
        "Threes": 0, 
        "Fours": 0, 
        "Fives": 0, 
        "Sixes": 0,
        "ThreeOfAKind": 0,
        "FourOfAKind": 0,
        "FullHouse":0,
        "Chance":0}

        cpt=0
        ThreeOfAKind = False    
        FourOfAKind = False
        FullhouseDouble = False
        FullhouseTriple = False
        for i in lancer:
            for cle, valeur in self.diccombo.items():
                if i == valeur:
                    resultats[cle] += i

        for cle, valeur in resultats.items():
            for cledic, valeurdic in self.diccombo.items():
                if cle == cledic:
                    if valeur>= 3 * valeurdic and valeur>0:
                        ThreeOfAKind = True
                    if valeur >= 4 * valeurdic and valeur>0:
                        FourOfAKind = True
                    #FULLHOUSE
                    if valeur== 3 * valeurdic and valeur>0:
                        FullhouseTriple = True
                    if valeur== 2 * valeurdic and valeur>0:
                        FullhouseDouble = True
            cpt+=valeur
 
        if ThreeOfAKind==True:
            resultats["ThreeOfAKind"] += cpt
        if FourOfAKind==True:
            resultats["FourOfAKind"] += cpt
        if FullhouseTriple and FullhouseDouble:
            resultats["FullHouse"] = 25

        
        resultats["Chance"] += cpt
        return resultats

        
game = Game()
lancer = [4,4,3,4,3]
print(game.lance(lancer))
