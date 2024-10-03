def solicitaDados(dado):
    return float(input("Informe "+dado))

def calculaImc(altura,peso):
    print(altura)
    print(peso)
    return(peso/(altura*altura))


def avaliaCategoriaImc(imc):
    if imc<18.5:
        return "Abaixo do peso"
    elif imc>=24.9:
        return "Normal"
    elif imc<=29.9:
        return "Sobrepeso"
    elif imc<=34.9:
        return "Obesidade Grau 1"
    elif imc<=39.9:
        return "Obesidade Grau 2"
    elif imc>40:
        return "Obesidade Grau 3"

def mostraImcCategoria(categoriaImc,imc):
    print("Categoria: {}\nIMC: {:.1}".format(categoriaImc,imc))

if __name__=="__main__":
    peso=solicitaDados("seu peso em Kg: ")
    altura=solicitaDados("sua altura em metros: ")
    imc=calculaImc(altura,peso)
    print(imc)
    categoriaImc=avaliaCategoriaImc(imc)
    mostraImcCategoria(categoriaImc,imc)