peso = float(input('Informe seu peso: Kg'))
altura = float(input('Informe sua altura: M'))
imc = peso/(altura**2)
if imc < 18.5:
    sit = 'Abaixo do peso'
elif imc < 25:
    sit = 'Peso ideal'
elif imc < 30:
    sit = 'Sobrepeso'
elif imc < 40:
    sit = 'Obesidade'
else:
    sit = 'Obesidade mórbida'
print('Seu IMC é {:.2f} você está na categoria: {}'.format(imc, sit))