from models import veiculos

def find_veiculo(veiculo_id: int):
    for veiculo in veiculos:
        if veiculo.id == veiculo_id:
            return veiculo
    return None
