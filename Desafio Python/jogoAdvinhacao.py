def solicitarPalpite():
    return int(input("Informe um palpite de 0 a 100\nInforme seu palpite: "))

def taQuenteOuFrio(palpite,numeroAleatorio,nome):
    if numeroAleatorio>palpite:
        print("Palpite de ",nome," foi muito baixo!")
    else:
        print("Palpite de ",nome," foi muito alto!")

def verificaPalpite():
    if palpite==numeroAleatorio:
        return True
    else:
        return False


import random
nome=(input("informe seu nome: "))
numeroAleatorio=random.randint(1,100)
contador = 10
for i in range(10,0,-1):
    palpite=solicitarPalpite()
    contador-=1
    if verificaPalpite():
        print("Parabens ",nome," Voce Ganhou!\n Voce levou ",contador," tentativas")
        resultado="ganhou"
        break
    else:
        taQuenteOuFrio(palpite,numeroAleatorio,nome)
        print("tentativas restantes: ",contador)
        resultado="perdeu"
if resultado == "perdeu":
    print("Voce perdeu!\n o numero era:", numeroAleatorio)     


    