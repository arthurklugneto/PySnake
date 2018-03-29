#   Objeto SCORE
#   
#   Cuida das rotinas de ui que mostram o ponto do jogador na tela
#
import globals

class Score(object):

    def draw(self,player,gameFont,frameBuffer):

        # desenha o texto com ponto dos jogadores na tela
        scoreSurface = gameFont.render("Score  :  " + str(player.getScore()), False, (0, 0, 0))
        frameBuffer.blit(scoreSurface,(10,globals.screenSize[1]+20))

