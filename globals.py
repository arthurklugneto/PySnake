import json

# variáveis de configuração
config = json.load(open('config.json'))                            # carrega arquivo de configuarção do jogo
playerSize = config["playerSize"]                                  # tamanho do player
screenSize = (config["screenWidth"],config["screenHeight"])        # tamanho da tela em pixels

# TODO : Carregar tudo isso do Json
# variaveis de jogo
clock = 0                                                                      
fps = 60                                                                       
refreshRate = config["refreshRate"]                                            
screenGridSize = (int(screenSize[0]/playerSize),int(screenSize[1]/playerSize))
playerColor = (0,0,0)                                                         
playerInitialPosition = [screenGridSize[0]/2,screenGridSize[1]/2]              
obstacleThreshold = config["obstacleThreshold"]                                
obstacleGradation = config["obstacleGradation"]                                
totalBoxCollectables = config["totalBoxCollectables"]                         
totalTriangleCollectables = config["totalTriangleCollectables"]                                      
totalCircleCollectables = config["totalCircleCollectables"]               
pointBox = config["pointBox"]
pointTriangle = config["pointTriangle"]
pointCircle = config["pointCircle"]
maxScore = config["maxScore"]
maxLevel = config["maxLevel"]
maxRefreshRate = config["maxRefreshRate"]