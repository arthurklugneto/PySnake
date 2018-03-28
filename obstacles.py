import globals
from random import randint

class Obstacles(object):

    __obstacles = []
    __mapSize = ""
    __color = (30,30,30)
    __size = 0

    def __init__(self):
        
        self.__mapSize = globals.screenGridSize
        self.__size = globals.playerSize

        for obstacle in range(globals.initialObstacles):

            obsX = randint(0,self.__mapSize[0])
            obsY = randint(0,self.__mapSize[1])
            self.__obstacles.insert(0,[obsX,obsY])

    def draw(self,frameBuffer,pygame):

        # frameBuffer.lock()
        # for position in self.__positions:
        #     frameBuffer.fill(self.__color,pygame.draw.rect(frameBuffer, self.__color, [position[0]*self.__size,position[1]*self.__size,self.__size,self.__size],1))
        # frameBuffer.unlock()
        
        frameBuffer.lock()
        for obstacle in self.__obstacles:
            frameBuffer.fill(self.__color,pygame.draw.rect(frameBuffer, self.__color, [obstacle[0]*self.__size,obstacle[1]*self.__size,self.__size,self.__size],1))
        frameBuffer.unlock()