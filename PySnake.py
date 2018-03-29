#
#   PySnake - Jogo de Snake em Python usando PyGame
#   Trabalho proposto pelo professor Kane Chan
#
#   Autores : Arthur Klug Neto E Luis Fernando de Souza
#

# --- CONFIGURAÇÕES INICIAIS ------------------------------------------------------------------------------------------------------------

# importação das bibliotecas utilizadas
import globals
import pygame
from util import *

# importação dos objetos
from mapa import Mapa
from player import Player
from score import Score
from obstacles import Obstacles
from collectables import Collectables

# mostra um texto de boas vindas
greetings()

# verifica se o mapa pode ser gerado com perfeição
if not verifyConfig(globals.screenSize,globals.playerSize):
    quit()
else:
    print("Iniciando o jogo...")
    if globals.config["debug"] : print("Modo de depuração ativado.")

# inicia o pygame e o mecanismo de texto
pygame.init()
pygame.font.init()

# inicia a surface que será o framebuffer da tela e define o titulo da janela
# define uma margem de 50 pixel na parte inferior para desenhar o score
frameBuffer = pygame.display.set_mode((globals.screenSize[0],globals.screenSize[1]+50))
pygame.display.set_caption(globals.config["title"])

# define a fonte do texto que será utilizado no jogo
gameFont = pygame.font.SysFont('Calibri', 16)

# define o relógio do jogo
globals.clock = pygame.time.Clock()
count = 0

# cria os objetos do jogo
mapa = Mapa()
player = Player()
score = Score()
obstacles = Obstacles()
collectables = Collectables(obstacles)

# --- LOOP PRINCIPAL DO JOGO ------------------------------------------------------------------------------------------------------------
try:
    while True:

        # pinta o fundo do mapa
        frameBuffer.fill((200,200,200))

        # o usuário fechou o jogo ?
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.sefDirection("LEFT")
            if event.key == pygame.K_RIGHT:
                player.sefDirection("RIGHT")
            if event.key == pygame.K_UP:
                player.sefDirection("UP")
            if event.key == pygame.K_DOWN:
                player.sefDirection("DOWN")
            if event.key == pygame.K_SPACE:
                player.setJustEat(True)

        if obstacles.checkCollisionWithPlayer(player.getPosition()):
            player.setIsDead(True)

        if not player.isDead :
            # atualiza o player a cada x milisegundos
            if count % globals.refreshRate == 0:
                player.update()

        mapa.draw(frameBuffer,pygame)
        player.draw(frameBuffer,pygame)
        score.draw(player,gameFont,frameBuffer)
        obstacles.draw(frameBuffer,pygame)
        collectables.draw(frameBuffer,pygame)

        # atualiza o framebuffer (desenha o que estiver na memória de vídeo)
        pygame.display.flip()

        # atualiza relógio
        globals.clock.tick(globals.fps)
        count += 1
finally:
   pygame.quit()







