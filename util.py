import globals

screenSize = globals.screenSize

def verifyConfig(screenSize,playerSize):
    if screenSize[0] > 320 and screenSize[1] > 240:
        if screenSize[0] % playerSize == 0 and screenSize[1] % playerSize == 0:
            if playerSize > 2:
                return True
    print("ERRO : O Tamanho da tela deve ser maior que 320x240 e o tamanho do player deve ser multiplo desses valores.")
    return False

def greetings():
    print(globals.config["title"])
    print("Versão  : " + globals.config["version"])
    print("Autores : " + globals.config["authors"])    