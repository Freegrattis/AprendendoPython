import random
from Ferramenta import Ferramenta
from Ferramenta110 import Ferramenta110
from Ferramenta220 import Ferramenta220
import Verificacao
import Limpeza

def cadastrar_ferramenta(tensao):
        nome = str(input("Digite o nome da ferramenta: \n=====================================\n"))
        Limpeza.limpar_tela()
        descricao = str(input("Digite o descricao da ferramenta: \n=====================================\n"))
        Limpeza.limpar_tela()
        marca = str(input("Digite o marca da ferramenta: \n=====================================\n"))
        Limpeza.limpar_tela()
        codigo = random.randint(0,1000)
        preco = Verificacao.verificar_preco("Digite o preço da ferramenta: \n=====================================\n")
        Limpeza.limpar_tela()
        quantidade_minima = Verificacao.verificar_inteiro("Digite a quantidade mínima em estoque: \n=====================================\n")
        Limpeza.limpar_tela()
        quantidade_atual = 0
        
        escolha = 0
        while escolha != "1" or escolha != "2":
            escolha = input("=== Selecione o tipo de tensão da ferramemnta ===\n[1] 110V\n[2] 220V\n=====================================\n")
            if escolha == "1":
                tensao = "110V"
                return Ferramenta110(nome, descricao, preco, marca, codigo,quantidade_minima, quantidade_atual, tensao)
            elif escolha == "2":
                tensao = "220V"
                return Ferramenta220(nome, descricao, preco, marca, codigo,quantidade_minima, quantidade_atual, tensao)
            else:
                print("\033[31;1mResposta inválida!\033[m")
                Limpeza.limpar_tela_timer()

def edita_ferramenta(codigo_informado, lista_ferramentas):
    for ferramenta in lista_ferramentas:
        if codigo_informado == Ferramenta.get_codigo(ferramenta):
            nome = str(input("Digite o nome da ferramenta: \n=====================================\n"))
            Limpeza.limpar_tela()
            descricao = str(input("Digite o descricao da ferramenta: \n=====================================\n"))
            Limpeza.limpar_tela()
            marca = str(input("Digite o marca da ferramenta: \n=====================================\n"))
            Limpeza.limpar_tela()
            preco = Verificacao.verificar_preco("Digite o preço da ferramenta: \n=====================================\n")
            Limpeza.limpar_tela()
            quantidade_minima = Verificacao.verificar_inteiro("Digite a quantidade mínima: \n=====================================\n")
            Limpeza.limpar_tela()
 
            Ferramenta.set_nome(ferramenta, nome)
            Ferramenta.set_descricao(ferramenta, descricao)
            Ferramenta.set_preco(ferramenta, preco)
            Ferramenta.set_marca(ferramenta, marca)
            Ferramenta.set_quantidade_minima(ferramenta, quantidade_minima)
            Limpeza.limpar_tela_timer()
            return print("==========================\n|       Alterado!        |\n==========================")
    return print("\033[31;1mCódigo não encontrado!\033[m")

def adiciona_ferramenta(codigo_informado, lista_ferramentas):
    for ferramenta in lista_ferramentas:
        if codigo_informado == Ferramenta.get_codigo(ferramenta):
            quantidade_nova = Verificacao.verificar_inteiro("Digite a quantidade a ser adicionada: \n========================================\n")
            quantidade_anterior = Ferramenta.get_quantidade_atual(ferramenta)
            quantidade_final = quantidade_anterior + quantidade_nova
            Ferramenta.set_quantidade_atual(ferramenta, quantidade_final) 
 
            return print("==========================\n|       Adicionado!       |\n==========================")
    Limpeza.limpar_tela_timer()
    return print("\033[31;1mCódigo não encontrado!\033[m")

def remove_ferramenta(codigo_informado, lista_ferramentas):
    for ferramenta in lista_ferramentas:
        if codigo_informado == Ferramenta.get_codigo(ferramenta):
            quantidade_remover = Verificacao.verificar_inteiro("Digite a quantidade a ser removida: \n========================================\n")
            if quantidade_remover <= Ferramenta.get_quantidade_atual(ferramenta):
                quantidade_anterior = Ferramenta.get_quantidade_atual(ferramenta)
                quantidade_final = quantidade_anterior - quantidade_remover
                Ferramenta.set_quantidade_atual(ferramenta, quantidade_final)
                return print("==========================\n|       Removido!        |\n==========================")
            else:
                return print("\033[31;1mNão pode remover uma quantidade maior do que tem no estoque!\033[m")
    Limpeza.limpar_tela_timer()
    return print("\033[31;1mCódigo não encontrado!\033[m")

def excluir_ferramenta(codigo_informado,lista_ferramentas):
    for ferramenta in lista_ferramentas:
        if(codigo_informado==Ferramenta.get_codigo(ferramenta)):
            if Ferramenta.get_quantidade_atual(ferramenta) == 0:
                lista_ferramentas.remove(ferramenta)
                return print("\033[31;1m==========================\n|       Excluido!        |\n==========================\033[m")
            else:
                return print("\033[31;1mAinda há quantidade em estoque!\033[m")
    return print("\033[31;1mCódigo não encontrado!\033[m")

def exibir_marca(lista_ferramentas):
    escolha = 0
    encontrado=False
    marca_procurada = input("Digite a marca a ser pesquisada: ")
    for ferramenta in lista_ferramentas:
        if Ferramenta.get_marca(ferramenta) == marca_procurada:
            print("\033[92;1m=== Produtos da Marca ===\033[m")
            print(f"Codigo: {ferramenta.get_codigo()}")
            print(f"Nome: {ferramenta.get_nome()}")
            print(f"Descrição: {ferramenta.get_descricao()}")
            print(f"Marca: {ferramenta.get_marca()}")
            print(f"Preço: R${str(ferramenta.get_preco()).replace(".",",")}")
            print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
            print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
            print(f"Tensão: {ferramenta.get_tensao()}")
            print("==================================")
            encontrado=True
    if not encontrado:
        print("\033[31;1mNão há ferramentas cadastradas com essa marca!\033[m")

    while escolha != "1":
        escolha = input("Deseja retornar ao menu? [1] Sim | [2] Não\n")
        if escolha == "1":
            break
        elif escolha == "2":
            continue
        else:
            print("\033[31;1mOpção selecionada inexistente!\033[m")

def exibir_tensao(lista_ferramentas):
    escolha_menu = 0
    escolha = input("=== Selecione o tipo de tensão da ferramemnta ===\n[1] 110V\n[2] 220V\n=====================================\n")
    if escolha == "1":
        tensao_procurada = "110V"
    elif escolha=="2":
        tensao_procurada = "220V"
    else:
        print("\033[31;1mResposta inválida!\033[m")
        return Limpeza.limpar_tela_timer()
    encontrado = False
    for ferramenta in lista_ferramentas:
        if ferramenta.get_tensao() == tensao_procurada:
                print("\033[92;1m=== Produtos da Tensão",tensao_procurada,"===\033[m")
                print(f"Codigo: {ferramenta.get_codigo()}")
                print(f"Nome: {ferramenta.get_nome()}")
                print(f"Descrição: {ferramenta.get_descricao()}")
                print(f"Marca: {ferramenta.get_marca()}")
                print(f"Preço: R${str(ferramenta.get_preco()).replace(".",",")}")
                print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
                print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
                print(f"Tensão: {ferramenta.get_tensao()}")
                print("==================================")
                encontrado = True    
    if not encontrado:
        print("\033[31;1mNão há ferramentas cadastradas com essa tensão!\033[m")
    while escolha_menu != "1":
        escolha_menu = input("Deseja retornar ao menu? [1] Sim | [2] Não\n")
        if escolha_menu == "1":
            break
        elif escolha_menu == "2":
            continue
        else:
            print("\033[31;1mOpção selecionada inexistente!\033[m")
                    

def verifica_necessidade_compra(lista_ferramentas):
    escolha = 0
    for ferramenta in lista_ferramentas:
        if ferramenta.get_quantidade_atual() <= ferramenta.get_quantidade_minima():
            print("\033[31;1m=== Necessita repôr estoque! ===\033[m")
            print(f"Codigo: {ferramenta.get_codigo()}")
            print(f"Nome: {ferramenta.get_nome()}")
            print(f"Descrição: {ferramenta.get_descricao()}")
            print(f"Marca: {ferramenta.get_marca()}")
            print(f"Preço: R${str(ferramenta.get_preco()).replace(".",",")}")
            print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
            print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
            print(f"Tensão: {ferramenta.get_tensao()}")
            print("==================================")
        else:
            print("\033[96;1m= Não há necessidade de compra! =\033[m")
            print(f"Codigo: {ferramenta.get_codigo()}")
            print(f"Nome: {ferramenta.get_nome()}")
            print(f"Descrição: {ferramenta.get_descricao()}")
            print(f"Marca: {ferramenta.get_marca()}")
            print(f"Preço: R${str(ferramenta.get_preco()).replace(".",",")}")
            print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
            print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
            print(f"Tensão: {ferramenta.get_tensao()}")
            print("==================================")
    while escolha != "1":
        escolha = input("Deseja retornar ao menu? [1] Sim | [2] Não\n")
        if escolha == "1":
            break
        elif escolha == "2":
            continue
        else:
            print("\033[31;1mOpção selecionada inexistente!\033[m")


def exibir_codigo(lista_ferramentas):
    encontrado = False
    escolha = 0
    codigo_procurado = Verificacao.verificar_inteiro("Digite o código do produto: ")
    for ferramenta in lista_ferramentas:
        if Ferramenta.get_codigo(ferramenta) == codigo_procurado:
            print("\033[94m=== Informações do Produto ===\033[m")
            print(f"Codigo: {ferramenta.get_codigo()}")
            print(f"Nome: {ferramenta.get_nome()}")
            print(f"Descrição: {ferramenta.get_descricao()}")
            print(f"Marca: {ferramenta.get_marca()}")
            print(f"Preço: R${str(ferramenta.get_preco()).replace(".",",")}")
            print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
            print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
            print(f"Tensão: {ferramenta.get_tensao()}")
            print("==================================")
            encontrado = True
    if not encontrado:
        print("\033[31;1mNão há ferramentas cadastradas com esse código!\033[m")
    while escolha != "1":
        escolha = input("Deseja retornar ao menu? [1] Sim | [2] Não\n")
        if escolha == "1":
            break
        elif escolha == "2":
            continue
        else:
            print("\033[31;1mOpção selecionada inexistente!\033[m")

def exibir_informacoes(lista_ferramentas):
    escolha = 0
    Limpeza.limpar_tela()
    for ferramenta in lista_ferramentas:
        print("\033[94m=== Informações do Produto ===\033[m")
        print(f"Codigo: {ferramenta.get_codigo()}")
        print(f"Nome: {ferramenta.get_nome()}")
        print(f"Descrição: {ferramenta.get_descricao()}")
        print(f"Marca: {ferramenta.get_marca()}")
        print(f"Preço: R${str(ferramenta.get_preco()).replace(".",",")}")
        print(f"Quantidade minima: {ferramenta.get_quantidade_minima()}")
        print(f"Quantidade atual: {ferramenta.get_quantidade_atual()}")
        print(f"Tensão: {ferramenta.get_tensao()}")
        print("=====================================")
    while escolha != "1":
        escolha = input("Deseja retornar ao menu? [1] Sim | [2] Não\n")
        if escolha == "1":
            break
        elif escolha == "2":
            continue
        else:
            print("\033[31;1mOpção selecionada inexistente!\033[m")