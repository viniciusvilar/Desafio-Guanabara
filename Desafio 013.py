sal = float(input("Digite o valor do salário: "))
valAum = (sal*15)/100
novoSal = sal + valAum
print("Salário: R${:.2f}".format(sal))
print("Valor do aumento de 15%: R${:.2f}".format(valAum))
print("Valor do salário com o aumento: R${:.2f}".format(novoSal))