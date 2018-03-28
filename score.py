import globals

class Score(object):

    def draw(self,player,gameFont,frameBuffer):

        scoreSurface = gameFont.render("Score  :  " + str(player.getScore()), False, (0, 0, 0))
        frameBuffer.blit(scoreSurface,(10,globals.screenSize[1]+20))

