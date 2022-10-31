num1 = float(input('Digite o valor da reta 1: '))
num2 = float(input('Digite o valor da reta 2: '))
num3 = float(input('Digite o valor da reta 3: '))
if (abs(num2-num3) < num1 < (num2+num3)) and (abs(num1-num3) < num2 < (num1+num3)) and (abs(num1-num2) < num3 < (num1+num2)):
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')