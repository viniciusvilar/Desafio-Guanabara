nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2)/2
if media < 5.0:
    sit = 'REPROVADO!'
elif media < 7.0:
    sit = 'RECUPERAÇÃO'
else:
    sit = 'APROVADO!'
print('Sua média é {:.1f}!'.format(media))
print('Você está {}'.format(sit))