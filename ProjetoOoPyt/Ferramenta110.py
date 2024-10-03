from Ferramenta import Ferramenta

class Ferramenta110(Ferramenta):
    def __init__(self, nome, descricao, preco, marca, codigo, quantidade_minima, quantidade_atual, tensao="110V"):
        super().__init__(nome, descricao, preco, marca, codigo, quantidade_minima, quantidade_atual)
        self.__tensao = tensao

    def get_tensao(self):
        return self.__tensao
    
    def set_tensao(self, tensao):
        self._tensao = tensao