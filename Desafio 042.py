num1 = float(input('Digite o valor da reta 1: '))
num2 = float(input('Digite o valor da reta 2: '))
num3 = float(input('Digite o valor da reta 3: '))
if (abs(num2-num3) < num1 < (num2+num3)) and (abs(num1-num3) < num2 < (num1+num3)) and (abs(num1-num2) < num3 < (num1+num2)):
    print('É possível formar um triângulo')
    if num1 == num2 and num1 == num3 and num2 == num3:
        tipo = 'Equilátero'
    elif num1 != num2 and num1 != num3 and num2 != num3:
        tipo = 'Escaleno'
    else:
        tipo = 'Isóceles'
    print('Este triângulo é do tipo: {}'.format(tipo))
else:
    print('Não é possível formar um triângulo')