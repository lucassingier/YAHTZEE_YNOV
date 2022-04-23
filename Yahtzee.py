class Game:
    diccombo = {
        "Ones": 1, 
        "Twos": 2,
        "Threes": 3, 
        "Fours": 4, 
        "Fives": 5, 
        "Sixes": 6 }
    
    def lance(self,lancer):
        resultats ={
        "Ones": 0, 
        "Twos": 0,
        "Threes": 0, 
        "Fours": 0, 
        "Fives": 0, 
        "Sixes": 0}
        cpt=0
        for i in lancer:
            for cle, valeur in self.diccombo.items():
                if i == valeur:
                    resultats[cle] += i
        return resultats
            
        

game = Game()
lancer = [1,1,1,2,5]
print(game.lance(lancer))
