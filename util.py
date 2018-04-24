#   Alguns métodos úteis para facilitar a nossa vida
import globals

screenSize = globals.screenSize

# verifica se o tamanho da tela e jogador
# são corretos para utilização
def verifyConfig(screenSize,playerSize):
    if screenSize[0] >= 200 and screenSize[1] >= 200:
        if screenSize[0] % playerSize == 0 and screenSize[1] % playerSize == 0:
            if playerSize >= 2:
                return True
    print("ERRO : O Tamanho da tela deve ser maior que 200x200 e o tamanho do player deve ser no minimo 2 e deve ser multiplo desses valores.")
    return False

# mostra mensagem de boas vindas
# no console antes de abrir a tela do jogo
def greetings():
    print(globals.config["title"])
    print("Versão  : " + globals.config["version"])
    print("Autores : " + globals.config["authors"])

'''
Arduino Map Function
long map(long x, long in_min, long in_max, long out_min, long out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
'''
def map(x,in_min,in_max,out_min,out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min