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
        "SmallStraight":0,
        "LargeStraight":0,
        "Chance":0,
        "Yahtzee":0}
    
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
        "SmallStraight":0,
        "LargeStraight":0,
        "Chance":0,
        "Yahtzee":0}

        cpt=0
        listUniqValues = []
        ThreeOfAKind = False    
        FourOfAKind = False
        FullhouseDouble = False
        FullhouseTriple = False
        Yahtzee = False
        for i in lancer:
            for cle, valeur in self.diccombo.items():
                if i == valeur:
                    resultats[cle] += i

        for cle, valeur in resultats.items():
            for cledic, valeurdic in self.diccombo.items():
                if cle == cledic and valeur>0:
                    #THREE&FOUR_OF_A_KIND
                    if valeur >= 3 * valeurdic:
                        ThreeOfAKind = True
                    if valeur >= 4 * valeurdic:
                        FourOfAKind = True
                        
                    #FULLHOUSE
                    if valeur== 3 * valeurdic:
                        FullhouseTriple = True
                    if valeur== 2 * valeurdic:
                        FullhouseDouble = True

                    #SMALL&LARGE_STRAIGHT
                    listUniqValues.append(valeurdic)

                    #YAHTZEE
                    if valeur == 5 * valeurdic:
                        Yahtzee = True
                    
            cpt+=valeur

        cptSuite = 0
        maxCptSuite = 0
        for i in range(len(listUniqValues)-1):
            if listUniqValues[i+1]-listUniqValues[i] == 1:
                cptSuite+=1
                if cptSuite > maxCptSuite:
                    maxCptSuite = cptSuite
            else:
                cptSuite=0
            
        if ThreeOfAKind:
            resultats["ThreeOfAKind"] += cpt
        if FourOfAKind:
            resultats["FourOfAKind"] += cpt
        if Yahtzee:
            resultats["Yahtzee"] = 50
        if FullhouseTriple and FullhouseDouble:
            resultats["FullHouse"] = 25
        if maxCptSuite >= 3:
            resultats["SmallStraight"] = 30
        if maxCptSuite == 4:
            resultats["LargeStraight"] = 40
        resultats["Chance"] += cpt
        return resultats

        
game = Game()
lancer = [1,2,4,5,6]
print(game.lance(lancer))
