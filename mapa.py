import globals

class Mapa(object):
    
    __mapSize = ""
    __playerSize = 0

    def __init__(self):

        self.__mapSize = globals.screenGridSize
        self.__playerSize = globals.playerSize

        if globals.config["debug"] :
            print("Iniciado novo mapa do jogo com tamanho : " + str(globals.screenGridSize) )

    def draw(self,frameBuffer,pygame):

        if globals.config["debug"]:
            for x in range(self.__mapSize[0]):
                for y in range(self.__mapSize[1]):
                    pygame.draw.rect(frameBuffer, (128,128,128), [x*self.__playerSize, y*self.__playerSize, self.__playerSize, self.__playerSize],1)