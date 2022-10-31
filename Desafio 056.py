menorIdadeMulher = 0
maiorIdadeHomem = 0
mediaIdade = 0
homemVelho = ''
for c in range(0, 4):
    print('='*25)
    nome = input('Nome {}ª pessoa: '.format(c+1))
    idade = int(input('Idade {}ª pessoa: '.format(c+1)))
    sexo = input('Sexo[M/F] {}ª pessoa: '.format(c+1)).strip().lower()
    mediaIdade += idade
    if sexo == 'f':
        if idade < 20:
            menorIdadeMulher += 1
    if sexo == 'm':
        if idade > maiorIdadeHomem:
            homemVelho = nome

print('='*35)
print('A média de idade do grupo é {:.2f} anos'.format(mediaIdade/4))
print('O homem mais velho é {}'.format(homemVelho))
print('{} mulher(es) tem menos de 20 anos'.format(menorIdadeMulher))
