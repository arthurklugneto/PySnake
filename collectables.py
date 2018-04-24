import globals
from random import randint

class Collectables(object):

    __collectablesBox = []
    __collectablesBoxColor = (0,200,0)
    __collectablesTriangles = []
    __collectablesTrianglesColor = (255,0,0)
    __collectablesCircle = []
    __collectablesCircleColor = (0,0,255)

    __mapSize = None
    __playerSize = None

    __obstacles = None

    def __init__(self,obstacles):

        self.__obstacles = obstacles
        self.__mapSize = globals.screenGridSize
        self.__playerSize = globals.playerSize

        # TODO : Verificar se os collectables não estão
        #        sendo criados um em cima dos outros ou
        #        nas bordas das telas

        # Gera as comidinhas!!!
        self.__generateCollectables()

    def update(self,player):

        pos = player.getPosition()

        if pos in self.__collectablesBox:
            self.__collectablesBox.remove(pos)
            player.setJustEat(True)
            player.addToScore(globals.pointBox)

        if pos in self.__collectablesTriangles:
            self.__collectablesTriangles.remove(pos)
            player.setJustEat(True)
            player.addToScore(globals.pointTriangle)

        if [pos[0]+1,pos[1]+1] in self.__collectablesCircle:
            self.__collectablesCircle.remove([pos[0]+1,pos[1]+1])
            player.setJustEat(True)
            player.addToScore(globals.pointCircle)

        # O Player comeu todos os colectáveis. Gere mais!!!
        if not self.__collectablesBox and not self.__collectablesTriangles and not self.__collectablesCircle:
            self.__generateCollectables()

    def __generateCollectables(self):
        
        # Cria os Triangle Collectables
        while len(self.__collectablesTriangles) < globals.totalTriangleCollectables:
            x = randint(0,self.__mapSize[0])
            y = randint(0,self.__mapSize[1])
            if not self.__obstacles.checkCollisionWithPlayer([x,y]):
                self.__collectablesTriangles.insert(0,[x,y]);

        # Cria os Circle Collectables
        while len(self.__collectablesCircle) < globals.totalCircleCollectables:
            x = randint(0,self.__mapSize[0])
            y = randint(0,self.__mapSize[1])
            if not self.__obstacles.checkCollisionWithPlayer([x,y]):
                self.__collectablesCircle.insert(0,[x,y]);                

        # Cria os BOX Collectables
        while len(self.__collectablesBox) < globals.totalBoxCollectables:
            x = randint(0,self.__mapSize[0])
            y = randint(0,self.__mapSize[1])
            if not self.__obstacles.checkCollisionWithPlayer([x,y]):
                self.__collectablesBox.insert(0,[x,y]);

    def draw(self,frameBuffer,pygame):

        for boxCollectable in self.__collectablesBox:
            frameBuffer.lock()
            frameBuffer.fill(self.__collectablesBoxColor,pygame.draw.rect(frameBuffer, self.__collectablesBoxColor, 
            [boxCollectable[0]*globals.playerSize,boxCollectable[1]*globals.playerSize,globals.playerSize,globals.playerSize],1))
            frameBuffer.unlock()

        for triangleCollectable in self.__collectablesTriangles:
            frameBuffer.lock()
            pygame.draw.polygon(frameBuffer, self.__collectablesTrianglesColor, 
            self.__triangleAtPosition([triangleCollectable[0]*self.__playerSize-1,triangleCollectable[1]*self.__playerSize-1]),                              
            1)
            frameBuffer.unlock()

        for circleCollectable in self.__collectablesCircle:
            frameBuffer.lock()
            pygame.draw.circle(frameBuffer, self.__collectablesCircleColor, 
            (circleCollectable[0]*self.__playerSize-(int(self.__playerSize/2)),circleCollectable[1]*self.__playerSize-(int(self.__playerSize/2))), int(self.__playerSize/2))
            frameBuffer.unlock()

    def __triangleAtPosition(self,pos):
        return [[pos[0]+(self.__playerSize/2), pos[1]],[pos[0], pos[1]+self.__playerSize],[pos[0]+self.__playerSize, pos[1]+self.__playerSize]]