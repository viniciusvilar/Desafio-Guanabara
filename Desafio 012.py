preco = float(input("Informe o preço: "))
valDesc = (preco*5)/100
novoPreco = preco - valDesc
print("O valor do desconto é R${:.2f} e o novo preço com desconto é R${:.2f}".format(valDesc, novoPreco))