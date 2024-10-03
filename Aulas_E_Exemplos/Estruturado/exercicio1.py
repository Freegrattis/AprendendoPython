def solicitaValor(contador):
    num=int(input(contador+"valor: "))
    return num

def verificaResultado(a,b,c):
    if(a>b and a>c):
        print("o maior valor é: ",a)
    elif(b>c):
        print("o maior valor é: ",b)
    else:
        print("o maior valor é:", c) 

if __name__=="__main__":
        contador="1°"
        a=solicitaValor(contador)
        maior=a
        contador="2°"
        b=solicitaValor(contador)
        contador="3°"
        c=solicitaValor(contador)
        
        verificaResultado(a,b,c)
