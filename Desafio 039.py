import datetime
anoNasc = int(input('Ano de nascimento: '))
anoAtual = datetime.datetime.now().year
idade = anoAtual-anoNasc
print('Quem nasceu em {} tem {} anos em {}'.format(anoNasc, idade, anoAtual))
if idade < 18:
    faltaAnos = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(faltaAnos))
    print('Seu alistamento será em {}.'.format(anoAtual+faltaAnos))
elif idade > 18:
    anoAtrasado = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(anoAtrasado))
    print('Seu alistamento foi em {}.'.format(anoAtual-anoAtrasado))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')