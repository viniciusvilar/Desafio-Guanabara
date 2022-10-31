sal = float(input('Informe seu salário: '))
if sal > 1250:
    valAum = (sal*10)/100
    porc = 10
else:
    valAum = (sal*15)/100
    porc = 15
print('Você recebeu um aumento de {}% equivalente a R${:.2f}. Seu novo salário é R${:.2f}'.format(porc, valAum, sal+valAum))

