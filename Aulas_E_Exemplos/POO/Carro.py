class Carro:
    def __init__(self,modelo,ano,cor):#construtor, inicia um objeto
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        
    
    def dirigir (self):
        print(f"{self.modelo} do ano {self.ano} de cor {self.cor} está em movimento.")
    
    #Criando e atribuindo valores ao objeto
carro1=Carro("Sedan","2019","Preto")
carro2=Carro("SUV","2015","Branco")
carro3=Carro("Hatch","2023","Vermelho")

    #Chamando métodos
carro1.dirigir()
carro2.dirigir()
carro3.dirigir()