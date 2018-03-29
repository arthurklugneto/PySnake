import globals
from random import randint
from perlin import *

class Obstacles(object):

    __obstacles = []
    __mapSize = ""
    __color = (80,80,80)
    __size = 0
    __noiseGenerator = 0

    def __init__(self):
        
        self.__mapSize = globals.screenGridSize
        self.__size = globals.playerSize
        self.__noiseGenerator = SimplexNoise()

        for x in range(self.__mapSize[0]):
            for y in range(self.__mapSize[1]):
                if self.__noiseGenerator.noise2(x/globals.obstacleGradation,y/globals.obstacleGradation) > globals.obstacleThreshold:
                    self.__obstacles.insert(0,[x,y])

    def draw(self,frameBuffer,pygame):

        frameBuffer.lock()
        for obstacle in self.__obstacles:
            frameBuffer.fill(self.__color,pygame.draw.rect(frameBuffer, self.__color, [obstacle[0]*self.__size,obstacle[1]*self.__size,self.__size,self.__size],1))
        frameBuffer.unlock()

    def checkCollisionWithPlayer(self,player):
        
        if self.__noiseGenerator.noise2(player[0]/globals.obstacleGradation,player[1]/globals.obstacleGradation) > globals.obstacleThreshold:
            return True
        return False
