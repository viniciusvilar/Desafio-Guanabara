aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input('Média de {}: '.format(aluno['nome'])))
if aluno['media'] > 6:
    aluno['sit'] = 'Aprovadp'
else:
    aluno['sit'] = 'Reprovado'
print('='*25)
print('Nome: {}'.format(aluno['nome']))
print('Média: {}'.format(aluno['media']))
print('Situação: {}'.format(aluno['sit']))
