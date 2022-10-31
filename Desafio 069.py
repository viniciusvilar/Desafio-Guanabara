maior18 = 0
qtdHomens = 0
qtdMulheres20 = 0
while True:
    sexo = 'h'
    flag = 'h'
    print('======== CADASTRAR PESSOA ========')
    idade = int(input('Informe sua idade: '))
    while sexo not in 'MF':
        sexo = input('Informe seu sexo [M/F]: ').strip().upper()
    if idade > 18:
        maior18 += 1
    if 'M' in sexo:
        qtdHomens += 1
    if (idade < 20) and 'F' in sexo:
        qtdMulheres20 += 1
    print('=' * 25)
    while flag not in 'SN':
        flag = input('Deseja continuar [S/N]: ').strip().upper()
    if 'N' in flag:
        break
print('======== RELATÓRIO ========')
print('Pessoas maiores de 18 anos: {}'.format(maior18))
print('Quantidade de homens cadastrados: {}'.format(qtdHomens))
print('Quantidde de mulheres com menos de 20 anos: {}'.format(qtdMulheres20))
