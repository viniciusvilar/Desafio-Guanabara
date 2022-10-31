import datetime
anoNasc = int(input('Informe o ano de nascimento do atleta: '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNasc
if idade <= 9:
    cat = 'MIRIM'
elif idade <= 14:
    cat = 'INFANTIL'
elif idade <= 19:
    cat = 'JUNIOR'
elif idade == 20:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print('O atleta tem {} anos'.format(idade))
print('Ele está na categoria: {}'.format(cat))