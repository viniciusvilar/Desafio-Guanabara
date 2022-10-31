distancia = float(input('Qual a distância da viagem em Km/h? '))
if distancia <= 200:
    valorViagem = 0.50 * distancia
else:
    valorViagem = 0.45 * distancia
print('O valor da viagem será de R${:.2f}'.format(valorViagem))