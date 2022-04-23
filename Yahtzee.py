class Game:
    diccombo = {
        "Ones": 1, 
        "Twos": 2,
        "Threes": 3, 
        "Fours": 4, 
        "Fives": 5, 
        "Sixes": 6,
        "ThreeOfAKind": 0,
        "FourOfAKind": 0}
    
    def lance(self,lancer):
        resultats ={
        "Ones": 0, 
        "Twos": 0,
        "Threes": 0, 
        "Fours": 0, 
        "Fives": 0, 
        "Sixes": 0,
        "ThreeOfAKind": 0,
        "FourOfAKind": 0}
        cpt=0
        ThreeOfAKind = False    
        FourOfAKind = False
        
        for i in lancer:
            for cle, valeur in self.diccombo.items():
                if i == valeur:
                    resultats[cle] += i
        for cle, valeur in resultats.items():
            if cle == "Ones":
                if valeur>=3:
                    ThreeOfAKind=True
                if valeur>=4:
                    FourOfAKind=True
            elif cle == "Twos":
                if valeur>=6:
                    ThreeOfAKind=True
                if valeur>=8:
                    FourOfAKind=True
            elif cle == "Threes":
                if valeur>=9:
                    ThreeOfAKind=True
                if valeur>=12:
                    FourOfAKind=True
            elif cle == "Fours":
                if valeur>=12:
                    ThreeOfAKind=True
                if valeur>=16:
                    FourOfAKind=True
            elif cle == "Fives":
                if valeur>=15:
                    ThreeOfAKind=True
                if valeur>=20:
                    FourOfAKind=True
            elif cle == "Sixes":
                if valeur>=18:
                    ThreeOfAKind=True
                if valeur>=24:
                    FourOfAKind=True
            cpt+=valeur
                    
        if ThreeOfAKind==True:
            resultats["ThreeOfAKind"] += cpt
        if FourOfAKind==True:
            resultats["FourOfAKind"] += cpt
        return resultats
            
        

game = Game()
lancer = [4,4,4,4,5]
print(game.lance(lancer))
