#   Objeto SCORE
#   
#   Cuida das rotinas de ui que mostram o ponto do jogador na tela
#
import globals

class Score(object):

    def draw(self,player,gameFont,frameBuffer):

        # desenha o texto com ponto dos jogadores na tela
        scoreSurface = gameFont.render("Score: "+ str(player.getScore()) +"  Level:" + str(player.getLevel()), True, (0, 0, 0))
        frameBuffer.blit(scoreSurface,(10,globals.screenSize[1]+20))

    def drawGameOver(self,player,gameFont,frameBuffer):

        gameOverSurface = gameFont.render("Game Over!", True, (255, 0, 0))
        gameOverSurface2 = gameFont.render("Game Over!", True, (0, 0, 0))
        frameBuffer.blit(gameOverSurface2,(
                        globals.screenSize[0]/2-68,
                        globals.screenSize[1]/2+2))
        frameBuffer.blit(gameOverSurface,(
                        globals.screenSize[0]/2-70,
                        globals.screenSize[1]/2))
