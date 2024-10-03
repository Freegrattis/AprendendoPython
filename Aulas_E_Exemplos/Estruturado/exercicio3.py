def solicitaNumero(contador):
    num=float(input(contador+"numero: "))
    return num
def somaNumeros(a,b,c):
    return a+b+c

def subtraiNumeros(a,b,c):
    return a-b-c

def divideNumeros(a,b,c):
    if b==0 and c==0:
        return "Não foi possivel realizar a operação!"
    else:
        divisao= str(a/b/c)
        return divisao

def multiplicaNumeros(a,b,c):
    return (a*b)*c

def verificaMaiorNumero(a,b,c):
    return max(a,b,c)

def verificaMenorNumero(a,b,c):
   return min(a,b,c)
    
def calculaMedia(a,b,c):
    return (a+b+c)/3

def mostraResultados(soma,subtracao,divisao,multiplicacao,maior,menor,media):
    print(f"Soma: {soma}\nSubtração: {subtracao}\nDivisão: {divisao}\nMultiplicação: {multiplicacao}\nMaior número: {maior}\nMenor número: {menor}\nMédia: {media}")
      
if __name__=="__main__":
    contador="1°"
    a=solicitaNumero(contador)

    contador="2°"
    b=solicitaNumero(contador)

    contador="3°"
    c=solicitaNumero(contador)

    soma=somaNumeros(a,b,c)
    subtracao=subtraiNumeros(a,b,c)
    divisao=divideNumeros(a,b,c)
    multiplicacao=multiplicaNumeros(a,b,c)
    maior=verificaMaiorNumero(a,b,c)
    menor=verificaMenorNumero(a,b,c)
    media=calculaMedia(a,b,c)
    mostraResultados(soma,subtracao,divisao,multiplicacao,maior,menor,media)