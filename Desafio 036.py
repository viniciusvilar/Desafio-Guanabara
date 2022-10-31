valCasa = float(input('Informe o valor da casa R$'))
salario = float(input('Informe o valor do seu salário R$'))
qtdAnos = int(input('Informe em quantos anos deseja pagar: '))
prestMensal = valCasa/(qtdAnos*12)
if prestMensal <= (salario*30)/100:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de {:.2f}'.format(valCasa, qtdAnos, prestMensal))
    print('Empréstimo Aprovado!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valCasa, qtdAnos, prestMensal))
    print('Seu empréstimo não pode ser aprovado!')