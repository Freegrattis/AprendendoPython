def solicitaNota(contador):
    nota=float(input(contador+"nota: "))
    return nota

def calculaMedia(nota1,nota2,nota3):
    media=(nota1+nota2+nota3)/3
    return media

def verificaMedia(media):
    if media<3.9:
        return"REPROVADO"
    elif(media<6.9):
        return"EM EXAME"
    else:
        return "APROVADO"

def informaSituacao(media,statusAluno):
    print(f"Situação: {statusAluno}\nMédia: {media:.2f}")
        
if __name__=="__main__":
        contador="1°"
        nota1=solicitaNota(contador)

        contador="2°"
        nota2=solicitaNota(contador)

        contador="3°"
        nota3=solicitaNota(contador)
        
        media=calculaMedia(nota1,nota2,nota3)
        statusAluno=verificaMedia(media)
        informaSituacao(media,statusAluno)