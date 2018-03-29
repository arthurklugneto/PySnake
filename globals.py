import json

# variáveis de configuração
config = json.load(open('config.json'))                            # carrega arquivo de configuarção do jogo
playerSize = config["playerSize"]                                  # tamanho do player
screenSize = (config["screenWidth"],config["screenHeight"])        # tamanho da tela em pixels

# TODO : Carregar tudo isso do Json
# variaveis de jogo
clock = 0                                                                      # permite contagem de FPS do jogo
fps = 60                                                                       # FPS do jogo. Igual no CS!!!
refreshRate = config["refreshRate"]                                                               # velocidade de atualização. menos é mais rápido
screenGridSize = (int(screenSize[0]/playerSize),int(screenSize[1]/playerSize)) # quantidade de quadrados do jogo
playerColor = (0,0,0)                                                          # cor do jogador
playerInitialPosition = [screenGridSize[0]/2,screenGridSize[1]/2]              # posicao inicial do jogador                                                        # quantidade de obstaculos iniciais
obstacleThreshold = config["obstacleThreshold"]                                                        # THD de obstáculos. -1 a 1. Quanto menor mais denso
obstacleGradation = config["obstacleGradation"]                                                         # Fator de divisão da gradação do algoritmo perlin de geração do mapa. Maior é mais suave
totalBoxCollectables = config["totalBoxCollectables"]                                                        # quantos quadrados criar
totalTriangleCollectables = config["totalTriangleCollectables"]                                                   # quantos quadrados criar
totalCircleCollectables = config["totalCircleCollectables"]                                                    # quantos quadrados criar
pointBox = config["pointBox"]
pointTriangle = config["pointTriangle"]
pointCircle = config["pointCircle"]