def solicitarValorVenda():
    return float(input("valor da venda: R$"))

def somaFor(quantidadeVendas):
    vendas=0.0
    for i in range(quantidadeVendas):
        vendas+=solicitarValorVenda()
    vendas += vendas*0.25
    print("o vendedor ",nome+", vendeu R$",vendas)

def somaWhile(quantidadeVendas):
    vendas=0.0
    contador=0
    while contador<quantidadeVendas:
        vendas+=solicitarValorVenda()
        contador+=1
    vendas += vendas*0.25
    print("o vendedor ",nome+", vendeu R$",vendas)

if __name__=="__main__":
    nome=input("insira seu nome: ")
    quantidadeVendas=int(input("Informe a quantidade de vendas: "))
    #somaFor(quantidadeVendas)
    somaWhile(quantidadeVendas)
    