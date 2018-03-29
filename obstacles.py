#   Objeto OBSTACLES
#   
#   Cuida das rotinas para geração de obstáculos no mapa aleatórios utilizando PerlinNoise 2D.
#

import globals
from random import randint
from perlin import *

class Obstacles(object):

    # parametros locais do objeto
    __obstacles = []                # coleção de posições [x,y] das paredes dos obstaculos
    __mapSize = 0                   # tamanho do mapa em quadrados
    __color = (128,128,128)            # cor dos obstáculos
    __size = 0                      # tamanho do player    
    __noiseGenerator = 0            # objeto SimplesNoise

    # construtor. gera a coleção de valores [x,y] a  adiciona
    # a obstacles[] que guarda os blocos que são obstáculos e
    # não podem ser ultrapassados pelo jogados. 
    def __init__(self):
        
        # busca o tamanho do mapa e jogador do arquivo global
        self.__mapSize = globals.screenGridSize
        self.__size = globals.playerSize

        # cria instância do motor de geração de perlin noise.
        self.__noiseGenerator = SimplexNoise()

        # para cada quadrado do mapa, calcula se ele deveria
        # ser uma parede ou espaço que o player pode  passar
        # faz isso utilizando perlin noise então fica pareci
        # do com aspecto de ilha.
        for x in range(self.__mapSize[0]):
            for y in range(self.__mapSize[1]):
                if self.__noiseGenerator.noise2(x/globals.obstacleGradation,y/globals.obstacleGradation) > globals.obstacleThreshold:
                    self.__obstacles.insert(0,[x,y])

    def draw(self,frameBuffer,pygame):

        # desenha o mapa no buffer de video baseado nas posicoes
        # dentro do array obstacles[]
        frameBuffer.lock()
        for obstacle in self.__obstacles:
            frameBuffer.fill(self.__color,pygame.draw.rect(frameBuffer, self.__color, [obstacle[0]*self.__size,obstacle[1]*self.__size,self.__size,self.__size],1))
        frameBuffer.unlock()

    def checkCollisionWithPlayer(self,player):
        
        # verifica se o player colidiu com uma parede dos
        # obstáculos
        if self.__noiseGenerator.noise2(player[0]/globals.obstacleGradation,player[1]/globals.obstacleGradation) > globals.obstacleThreshold:
            return True
        return False
