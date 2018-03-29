import json

# variáveis de configuração
config = json.load(open('config.json'))                            # carrega arquivo de configuarção do jogo
playerSize = config["playerSize"]                                  # tamanho do player
screenSize = (config["screenWidth"],config["screenHeight"])        # tamanho da tela em pixels

# TODO : Carregar tudo isso do Json
# variaveis de jogo
clock = 0                                                                      # permite contagem de FPS do jogo
fps = 60                                                                       # FPS do jogo. Igual no CS!!!
refreshRate = 30                                                               # velocidade de atualização. menos é mais rápido
screenGridSize = (int(screenSize[0]/playerSize),int(screenSize[1]/playerSize)) # quantidade de quadrados do jogo
playerColor = (0,0,0)                                                          # cor do jogador
playerInitialPosition = [screenGridSize[0]/2,screenGridSize[1]/2]              # posicao inicial do jogador                                                        # quantidade de obstaculos iniciais
obstacleThreshold = 0.5                                                        # THD de obstáculos. -1 a 1. Quanto menor mais denso
obstacleGradation = 20                                                         # Fator de divisão da gradação do algoritmo perlin de geração do mapa. Maior é mais suave
totalBoxCollectables = 4                                                        # quantos quadrados criar
totalTriangleCollectables = 4                                                   # quantos quadrados criar
totalCircleCollectables = 4                                                     # quantos quadrados criar