

class Game:
    
    def lance(self,lancer):
        cpt=0
        for i in lancer:
            if (i == 1):
                cpt +=1
        return cpt

game = Game()
lancer = [1,1,1,2,5]
print(game.lance(lancer))