import datetime
anoAtual = datetime.datetime.now().year
maiorIdade = 0
menosIdade = 0
for c in range(0, 7):
    anoNasc = int(input('Informe o ano de seu nascimento: '))
    if (anoAtual - anoNasc) >= 21:
        maiorIdade += 1
    else:
        menosIdade += 1
print('Pessoas maior de idade: {}'.format(maiorIdade))
print('Pessoas menor de idade: {}'.format(menosIdade))