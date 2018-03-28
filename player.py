import globals

class Player(object):

    __positions = [[0,0],[0,0],[0,0]]
    __mapSize = ""
    __size = 0
    __color = ""
    __direction = "DOWN"

    isDead = True

    def __init__(self):
        self.__mapSize = globals.screenGridSize
        self.__positions = [[10,10],[10,11],[10,12]]
        self.__size = globals.playerSize
        self.__color = globals.playerColor
        self.isDead = False

    def draw(self,frameBuffer,pygame):
        frameBuffer.lock()
        for position in self.__positions:
            frameBuffer.fill(self.__color,pygame.draw.rect(frameBuffer, self.__color, [position[0]*self.__size,position[1]*self.__size,self.__size,self.__size],1))
        frameBuffer.unlock()

    def update(self):
        for index, position in enumerate(self.__positions):
            if self.__direction == "DOWN":
                position[1] += 1