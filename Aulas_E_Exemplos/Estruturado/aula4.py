#LAÇO DE REPETIÇÃO

def tabuada():
    numero=int(input("Informe um numero: "))
    for i in range(11):
        print(numero*i)
    print("fim")

def somaOrdenada():
    total=0
    for num in range(101):
        total=total+num
    print(total)

def ordemCrescente():
    for i in range(11):
        print(i)

def ordemDecrescente():
    for i in range(10, -1, -1):
        print(i)

def par():
    for i in range(0,11,2):
        print(i)

def impar():
    for i in range(1, 11, 2):
        print(i)
    
def testeWhile():
    contador=0
    while contador < 5:
        print(contador)
        contador+=1
        
def loopWhile():
    numeroSecreto=2
    print("adivinhe o numero secreto de 0 a 10!")
    palpite=int(input("digite seu palpite (0 a 10): \n"))
    while palpite != numeroSecreto:
        print("palpite incorreto. Tente novamente!")
        palpite=int(input("digite seu palpite (0 a 10):\n"))
    print("Parabens!")

import time
def main():
    contagemRegressiva=10
    while contagemRegressiva>-1:
        print(contagemRegressiva)
        contagemRegressiva=contagemRegressiva-1

        time.sleep(1)
        if contagemRegressiva==5: break
    print ("Contagem finalizada!")

import random
def numeroRandom():
    numeroAleatorio=random.randint(1,10)
    print(numeroAleatorio)

    numeroAleatorioFloat=random.random()
    print(numeroAleatorioFloat)

def listaRandom():
    lista=[1,2,3,4,5]
    random.shuffle(lista)#embaralha lista
    print("lista embaralhada: ",lista)

    elementoAleatorio=random.choice(lista)
    print("elemento aleatorio: ",elementoAleatorio)

if __name__=="__main__":
    listaRandom()
