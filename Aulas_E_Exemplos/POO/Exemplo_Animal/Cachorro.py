class Cachorro(Animal):
    def __init__(self,nome,raca):
        super().__init__(nome)
        self.raca=raca
    
    def fazer_som(self):
        return "Au au!"

    def abanar_rabo(self):
        return "Rabo abanado!"