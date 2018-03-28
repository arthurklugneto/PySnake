import globals

class Player(object):

    __positions = ""
    __mapSize = ""
    __size = 0
    __color = ""
    __direction = "LEFT"

    isDead = True

    def __init__(self):

        initialPosition = globals.playerInitialPosition

        self.__mapSize = globals.screenGridSize
        self.__positions = [initialPosition,
        [initialPosition[0],initialPosition[1]-1],
        [initialPosition[0],initialPosition[1]-2],
        [initialPosition[0],initialPosition[1]-3],
        [initialPosition[0],initialPosition[1]-4]]
        self.__size = globals.playerSize
        self.__color = globals.playerColor
        self.isDead = False

    def draw(self,frameBuffer,pygame):
        frameBuffer.lock()
        for position in self.__positions:
            frameBuffer.fill(self.__color,pygame.draw.rect(frameBuffer, self.__color, [position[0]*self.__size,position[1]*self.__size,self.__size,self.__size],1))
        frameBuffer.unlock()

    def update(self):
        
        self.__positions.pop()
        first = self.__positions[0]

        if self.__direction == "DOWN":
            self.__positions.insert(0,[ first[0],first[1]+1 ])
        if self.__direction == "RIGHT":
            self.__positions.insert(0,[ first[0]+1,first[1] ])
        if self.__direction == "LEFT":
            self.__positions.insert(0,[ first[0]-1,first[1] ])
        if self.__direction == "UP":
            self.__positions.insert(0,[ first[0],first[1]-1 ])

        self.checkDeath()
    
    def sefDirection(self,newDirection):
        self.__direction = newDirection

    def checkDeath(self):
        
        # Verifica colisão com as bordas
        headPosition = self.__positions[0]
        if headPosition[0] < 1 or headPosition[0] > self.__mapSize[0]-2 :
            self.isDead = True
        if headPosition[1] < 1 or headPosition[1] > self.__mapSize[1]-2 :
            self.isDead = True