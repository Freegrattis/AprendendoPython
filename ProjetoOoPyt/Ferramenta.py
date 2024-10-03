class Ferramenta():
    def __init__(self, nome, descricao, preco, marca, codigo,quantidade_minima,quantidade_atual):
        self.__nome = nome
        self.__descricao = descricao
        self.__preco = preco
        self.__marca = marca 
        self.__codigo = codigo
        self.__quantidade_minima=quantidade_minima
        self.__quantidade_atual=quantidade_atual


    def get_quantidade_minima(self):
        return self.__quantidade_minima

    def set_quantidade_minima(self, value):
        self.__quantidade_minima = value

    def get_quantidade_atual(self):
        return self.__quantidade_atual

    def set_quantidade_atual(self, value):
        self.__quantidade_atual = value

    def get_nome(self):
        return self.__nome

    def set_nome(self, value):
        self.__nome = value

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, value):
        self.__descricao = value

    def get_preco(self):
        return self.__preco

    def set_preco(self, value):
        self.__preco = value

    def get_marca(self):
        return self.__marca

    def set_marca(self, value):
        self.__marca = value

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, value):
        self.__codigo = value
        

        
        

    