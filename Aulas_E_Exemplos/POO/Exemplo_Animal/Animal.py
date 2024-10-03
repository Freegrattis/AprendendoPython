class Animal:
    def __init__(self,nome):
        self.nome=nome

    def fazer_som(self):
        pass

cachorro= Cachorro("Rex","Labrador")
gato= Gato("whiskers","Cinza")

print(cachorro.raca)
print (gato.cor)

print(cachorro.abanar_rabo())
print(gato.afiar_garras())