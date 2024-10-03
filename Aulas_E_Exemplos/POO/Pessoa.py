class Pessoa:
    def __init__(self,nome,idade,telefone,endereco):
        self.nome=nome
        self.idade=idade
        self.telefone=telefone
        self.endereco=endereco
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
        print(f"Meu telefone é {self.telefone} e meu endereço é: {self.endereco}")

pessoa1=Pessoa("João",30,"(47)9999-9999","Rua sla - 177")
pessoa1.apresentar()