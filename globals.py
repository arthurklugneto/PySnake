import json

# variáveis de configuração
config = json.load(open('config.json'))                            # carrega arquivo de configuarção do jogo
playerSize = config["playerSize"]                                  # tamanho do player
screenSize = (config["screenWidth"],config["screenHeight"])        # tamanho da tela em pixels (800x600)

# variaveis de jogo
clock = 0                                                                      # permite contagem de FPS do jogo
fps = 60                                                                       # FPS do jogo. Igual no CS!!!
refreshRate = 5                                                                # velocidade de atualização. menos é mais rápido
screenGridSize = (int(screenSize[0]/playerSize),int(screenSize[1]/playerSize)) # quantidade de quadrados do jogo
playerColor = (0,0,0)                                                          # cor do jogador
playerInitialPosition = [screenGridSize[0]/2,screenGridSize[1]/2]              # posicao inicial do jogador