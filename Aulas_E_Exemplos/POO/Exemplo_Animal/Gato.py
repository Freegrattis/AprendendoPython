class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome)
        self.cor=cor
    
    def fazer_som(self):
        return "Miau!"

    def afiar_garras(self):
        return "Garras sendo afiadas!"