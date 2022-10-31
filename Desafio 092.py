from datetime import datetime
dadosTrabalhador = dict()
anoAtual = datetime.now().year
dadosTrabalhador['nome'] = input('Nome: ')
dadosTrabalhador['idade'] = anoAtual - (int(input('Ano de Nascimento: ')))
dadosTrabalhador['ctps'] = int(input('Carteira de Trabalho [0 não tem]: '))
if dadosTrabalhador['ctps'] != 0:
    dadosTrabalhador['anoContrat'] = int(input('Ano de contratação: '))
    dadosTrabalhador['salario'] = float(input('Salário: '))
    dadosTrabalhador['idadeAposent'] = (35 - (anoAtual - dadosTrabalhador['anoContrat']) + dadosTrabalhador['idade'])
    print('Nome: {}'.format(dadosTrabalhador['nome']))
    print('Idade: {} anos'.format(dadosTrabalhador['idade']))
    print('Carteira de Trabalho: {}'.format(dadosTrabalhador['ctps']))
    print('Salário: R${:.2f}'.format(dadosTrabalhador['salario']))
    print('Idade de aposentadoria: {} anos'.format(dadosTrabalhador['idadeAposent']))
else:
    print('Nome: {}'.format(dadosTrabalhador['nome']))
    print('Idade: {} anos'.format(dadosTrabalhador['idade']))
    print('Carteira de Trabalho: {}'.format(dadosTrabalhador['ctps']))

