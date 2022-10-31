totalGasto = prodMais1000 = 0
prodBarato = ''
c = 1
while True:
    print('======= COMPRA =======')
    flag = 'h'
    nomeProduto = input('Nome do produto: ')
    precoProduto = float(input('Preço: R$'))
    if c == 1:
        nomeProdBarato = nomeProduto
        precoProdBarato = precoProduto
        c = 2
    elif precoProduto < precoProdBarato:
        nomeProdBarato = nomeProduto
        precoProdBarato = precoProduto
    totalGasto += precoProduto
    if precoProduto > 1000:
        prodMais1000 += 1
    while flag not in 'SN':
        flag = input('Deseja continuar [S/N]: ').strip().upper()
    if 'N' in flag:
        break
print('======= REL. COMPRA =======')
print('Total gasto: R${:.2f}'.format(totalGasto))
print('Produtos com valorr acuna de R$1000,00: {}'.format(prodMais1000))
print('Produto mais barato: {} R${:.2f}'.format(nomeProdBarato, precoProdBarato))
