class Game:
    
    def lance(self,lancer,num):
        cpt=0
        for i in lancer:
            if (i == num):
                cpt+=num
        return cpt

game = Game()
lancer = [2,1,2,2,2]
print(game.lance(lancer,2))
