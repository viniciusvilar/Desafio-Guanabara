from datetime import datetime

def voto(anoNasc):
    global idade
    anoAtual = datetime.now().year
    idade = anoAtual - anoNasc
    if idade >= 65:
        return 'VOTO OPCIONAL'
    elif idade >= 18:
        return 'VOTO OBRIGATÓRIO'
    elif idade >= 16:
        return 'VOTO OPCIONAL'
    else:
        return 'NÃO VOTA'

idade = 0
anoNasc = int(input('Ano de nascimento: '))
condVoto = voto(anoNasc)
print('Com {} anos: {}'.format(idade, condVoto))
