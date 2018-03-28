import globals

screenSize = globals.screenSize

def verifyConfig(screenSize,playerSize):
    if screenSize[0] >= 200 and screenSize[1] >= 200:
        if screenSize[0] % playerSize == 0 and screenSize[1] % playerSize == 0:
            if playerSize >= 4:
                return True
    print("ERRO : O Tamanho da tela deve ser maior que 200x200 e o tamanho do player deve ser no minimo 4 e deve ser multiplo desses valores.")
    return False

def greetings():s
    print(globals.config["title"])
    print("Versão  : " + globals.config["version"])
    print("Autores : " + globals.config["authors"])    