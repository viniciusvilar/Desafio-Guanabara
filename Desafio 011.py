larg = float(input("Qual a lagura da parede em metros? "))
altura = float(input("Qual a altura da parede em metros? "))
area = larg * altura
qtdTinta = area / 2
print("A área de sua parede é {:.2f}m2 e será necessário {}L de tinta para pintá-la".format(area, qtdTinta))