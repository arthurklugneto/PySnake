#   Objeto MAPA
#
#   Cuida das rotinas pertinentes a gerenciamento do mapa do jogo exceto obstáculos e collectables
#
import globals

class Mapa(object):
    
    # parametros locais do objeto
    __mapSize = ""                      # tamanho do mapa em quadrados
    __playerSize = 0                    # tamanho do player em px2 sera carregado do globals

    def __init__(self):

        # busca o tamanho do mapa e player do arquivo global
        self.__mapSize = globals.screenGridSize
        self.__playerSize = globals.playerSize

        # se estiver em modo de depuração, avise o jogador sobre o tamanho do mapa criado
        if globals.config["debug"] :
            print("Iniciado novo mapa do jogo com tamanho : " + str(globals.screenGridSize) )

    def draw(self,frameBuffer,pygame):

        # TODO : Isso é ineficiente!!! Monte esse grid em um surface
        # e desenhe o surface para não precisar passar por esse loop
        # toda vez que for desenhar a tela
        if globals.config["debug"]:
            for x in range(self.__mapSize[0]):
                for y in range(self.__mapSize[1]):
                    pygame.draw.rect(frameBuffer, (128,128,128), [x*self.__playerSize, y*self.__playerSize, self.__playerSize, self.__playerSize],1)