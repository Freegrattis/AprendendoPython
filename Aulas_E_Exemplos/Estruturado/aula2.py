#Exemplo 1
""" base=float(input("Digite a base:"))
altura=float(input("Digite a altura:"))
area=base*altura
print("area retangulo =",area) """

#Exemplo2
""" area ="ETS"
idade=60
print(area,"POSSUI",idade,"ANOS DE TRADIÇÃO")

print(type(area))
type(area)  """

#Exemplo3
""" nome="alice"
idade=30
mensagem=f"Olá, meu nome é {nome} e tenho {idade} anos."
print(mensagem) """

#Exemplo4
""" dia_inicio_ferias=18
dia_final_ferias=31
mes="DEZEMBRO"
ano=2023
print('AS FERIAS SERÃO RETIRADAS ENTRE O DIA {} E O DIA {} DO MÊS DE {} DO ANO DE {}'.format(dia_inicio_ferias,dia_final_ferias,mes,ano)) """

#Exemplo5 - Ordem nos parâmetros
""" numero_1=10
numero_2=20
print('ESSE É O SEGUNDO PARÂMETRO: {1} ESSE É O PRIMEIRO PARÂMETRO: {0}.'.format(numero_1,numero_2))
"""

#Exemplo6 - Formatação

    #String
"""empresa = 'ROBERT BOSCH LTDA'
print (f'TRABALHO NA {empresa}')
print(f'TRABALHO NA {empresa.lower()}')

    #Floats
peso=70.12
print("O JOÃO PESA {} Kg.".format(peso))

peso=70.12
print("O JOÃO PESA {:f} Kg.".format(peso))

peso=70.12
print("O JOÃO PESA {:.2f} Kg.".format(peso))

peso=70.12
print("O JOÃO PESA {:6.2f} Kg.".format(peso))#{:numero de casa antes da virgula.numero de casa depois da virgula}

peso=70.12
print("O JOÃO PESA {:06.2f} Kg.".format(peso))

    #Inteiros
dia=8
mes=1
ano=2024
print(" DATA DE HOJE {:02d}/{:02d}/{:d}".format(dia,mes,ano))"""

#Exercicio7
""" sobrenome='Reis'
nome='Gabriel'
print("O NOME DO FUNCIONARIO É {1} {0}".format(sobrenome,nome)) """

#Exercicio8
""" area='ETS'
empresa='Robert Bosch Ltda'
print(area+empresa)
print(area,empresa) """