#   Objeto PLAYER
#   
#   Cuida das rotinas do jogador
#

import globals

class Player(object):

    # parametros locais do objeto
    __positions = ""
    __mapSize = ""
    __size = 0
    __color = ""
    __direction = "LEFT"
    __score = 0
    __level = 1
    __needToGrow = False

    # o player morreu?
    isDead = False

    def __init__(self):

        # carrega posição inicial do po player    
        initialPosition = globals.playerInitialPosition

        # TODO : Certificar-se que o player não seja
        #        criado dentro de um obstáculo

        # carrega o tamanho do mapa
        self.__mapSize = globals.screenGridSize
        # cria 3 blocos inicias para o player        
        self.__positions = [
        [int(initialPosition[0]),int(initialPosition[1])],
        [int(initialPosition[0]),int(initialPosition[1])-1],
        [int(initialPosition[0]),int(initialPosition[1])-2]]
        # carrega tamanho e cor do player
        self.__size = globals.playerSize
        self.__color = globals.playerColor
        # player não está morto!
        self.isDead = False

    def resetPlayer(self):
        # carrega posição inicial do po player    
        initialPosition = globals.playerInitialPosition

        #reinicia o player
        self.__positions = [
        [int(initialPosition[0]),int(initialPosition[1])],
        [int(initialPosition[0]),int(initialPosition[1])-1],
        [int(initialPosition[0]),int(initialPosition[1])-2]]

        self.__direction = "LEFT"

        # player não está morto!
        self.isDead = False


    def draw(self,frameBuffer,pygame):

        # desenha cada bloco do player
        frameBuffer.lock()
        for position in self.__positions:
            frameBuffer.fill(self.__color,pygame.draw.rect(frameBuffer, self.__color,[position[0]*self.__size,position[1]*self.__size,self.__size,self.__size],1))
        frameBuffer.unlock()

    def update(self):
        
        # aumenta o tamanho do player caso ele tenha
        # acabado de comer um collectable
        if self.__needToGrow:
            self.__needToGrow = False
        else:
            self.__positions.pop()

        # atualiza os blocos do player para que ele
        # possa ser movimentado
        first = self.__positions[0]

        # movimentos verticais e horizontais
        if self.__direction == "DOWN":
            self.__positions.insert(0,[ first[0],first[1]+1 ])
        if self.__direction == "RIGHT":
            self.__positions.insert(0,[ first[0]+1,first[1] ])
        if self.__direction == "LEFT":
            self.__positions.insert(0,[ first[0]-1,first[1] ])
        if self.__direction == "UP":
            self.__positions.insert(0,[ first[0],first[1]-1 ])

        # movimentos diagonais
        if self.__direction == "DOWN-RIGHT":
            self.__positions.insert(0,[ first[0]+1,first[1]+1 ])
        if self.__direction == "DOWN-LEFT":
            self.__positions.insert(0,[ first[0]-1,first[1]+1 ])
        if self.__direction == "UP-RIGHT":
            self.__positions.insert(0,[ first[0]+1,first[1]-1 ])
        if self.__direction == "UP-LEFT":
            self.__positions.insert(0,[ first[0]-1,first[1]-1 ])
            
        # verifica se o player morreu
        self.checkDeath()
    
    # altera a direção em que o player está de movimentando
    def sefDirection(self,newDirection):
        
       self.__direction = newDirection

    def checkDeath(self):
        
        # Verifica colisão com as bordas da janela
        headPosition = self.__positions[0]
        if headPosition[0] < 1 or headPosition[0] > self.__mapSize[0]-2 :
            self.isDead = True
        if headPosition[1] < 1 or headPosition[1] > self.__mapSize[1]-2 :
            self.isDead = True

        # Verifica colisão com próprio corpo
        for idx,pos in enumerate(self.__positions):
            if idx!=0 and pos == headPosition:
                self.isDead = True

    # retorna o score do player
    def getScore(self):
        return self.__score

    # retorna a posição atual do jogador
    def getPosition(self):
        return self.__positions[0]

    # em que nível o jogador está
    def getLevel(self):
        return self.__level

    # define se o player está morto
    def setIsDead(self,value):
        self.isDead = value

    # define que o player acabou de comer um collectable
    def setJustEat(self,value):
        self.__needToGrow = value

    # adiciona ao ponto do jogador
    def addToScore(self,value):
        self.__score += value

    # troca o nível do jogador
    def setLevel(self,value):
        self.__level = value