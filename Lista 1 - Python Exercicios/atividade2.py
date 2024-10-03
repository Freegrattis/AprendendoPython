

def fatorialWhile(numero):
    resultado=1
    cont=1
    while cont <= numero:
        resultado *= cont
        cont += 1
    print(resultado)

def fatorialFor(numero):
    resultado=1
    
    for i in range(1,numero+1):
        resultado*=i
    print(resultado)

if __name__=="__main__":
    numero=int(input("Informe um numero para ver o fatorial: \n"))
    print("FOR")
    fatorialFor(numero)
    print('\n')
    print("WHILE")
    fatorialWhile(numero)