valorPag = float(input('Informe o valor a ser pago: R$ '))
print('='*30)
print('MENU DE OOÇÃO')
print('1 ------ À VISTA (DIN/CHEQUE)')
print('2 ----- À VISTA (CARTÃO)')
print('3 ----- EM ATÉ 2X (CARTÃO)')
print('4 ----- 3X OU MAIS (CARTÃO)')
print('='*30)
op = int(input('Selecione a oção: '))
if op == 1:
    desc = (10*valorPag)/100
    sit = 'Você terá um desconto de 10% no valor de R${:.2f}. Você pagará R${:.2f}!'.format(desc, valorPag-desc)
elif op == 2:
    desc = (5*valorPag)/100
    sit = 'Você terá um desconto de 5% no valor de R${:.2f}. Você pagará R${:.2f}!'.format(desc, valorPag-desc)
elif op == 3:
    sit = 'Sua compra manteve o mesmo preço. Você pagará 2 parcelas no valor de R${:.2f}!'.format(valorPag/2)
elif op == 4:
    qtdParc = int(input('Quantas parcelas? '))
    acres = (20*valorPag)/100
    novoValorPag = valorPag + acres
    valParc = novoValorPag / qtdParc
    sit = 'Sua compra teve um acréscimo de 20% de juros no valor de R${:.2f}. Você pagará R${:.2f} em {} parcelas de R${:.2f}!'.format(acres, novoValorPag, qtdParc, valParc)
else:
    sit = 'Você digitou um valor inexistente. O programa será encerrado!'
print(sit)