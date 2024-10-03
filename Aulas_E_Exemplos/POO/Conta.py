class Conta:
    def __init__(self,numero,titular,saldo,limite=1000.0):
        self.__numero=numero
        self.__titular=titular
        self.__saldo =saldo#Variavel privada
        self.__limite =limite#Variavel privada

    def get_numero(self):
        return self.__numero
    def set_numero(self,numero):
        self.__numero=numero

    def get_titular(self):
        return self.__titular
    def set_titular(self,titular):
        self.__titular=titular

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,saldo):
        self.__saldo=saldo

    def get_limite(self):
        return self.__limite
    def set_limite(self,limite):
        self.__limite=limite
    
    def depositar(self,valor):
        self.saldo+=valor
        print(f"Deposito de R${valor} realizado. Novo saldo: R${self.saldo}")

    def __sacar(self,valor):#Metodo privado
        if self.saldo-valor>=-self.limite:
            self.saldo+=valor
            print(f"Saque de R${valor} realizado. Novo saldo: R${self.saldo}")
        else:
            print("Saldo Insuficiente. Operação não realizada")
    
    def transferir(self,destino,valor):
        if self.saldo-valor>=-self.limite:
            self.saldo-=valor
            destino.saldo+=valor
            print(f"Transferência de R${valor} realizada para conta de {destino.titular}.")
        else:
            print("Saldo Insuficiente. Operação não realizada")

conta=Conta(123,"Fulano",1000.0)
print(conta.get_numero())

conta.set_numero(456)
print(conta.get_numero())

conta.set_saldo(1500.0)
print(conta.get_saldo()) 