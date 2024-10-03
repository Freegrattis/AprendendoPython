import re
import Limpeza

def verificar_inteiro(texto):
    while True:
        try:
            return int(input(texto))
        except Exception:
            print("\033[31;1mERROR! Digite um valor válido\033[m")
            Limpeza.limpar_tela_timer()
        else:
            break

def verificar_float(texto):
    while True:
        try:
            return float(input(texto))
        except Exception:
            print("\033[31;1mERROR! Digite um valor válido\033[m")
        else:
            break

def verificar_preco(texto):
    while True:
        try:

            valor = input(texto)

            padrao = r"([0-9,])+"
            verific = re.match(padrao, valor)

            if verific:
                valor = valor.replace(",",".")
                return float(valor)
            
            print("\033[31;1mERROR! Digite um valor válido\033[m")
            Limpeza.limpar_tela_timer()
        except Exception:
            print("\033[31;1mERROR! Digite um valor válido\033[m")
