veloc = float(input('Velocidade do carro: '))
if veloc > 80:
    velocExc = veloc - 80
    valMulta = velocExc * 7
    print("Você excedeu o limite de 80km/h e recebeu uma multa no valor de R${:.2f}!".format(valMulta))
#else:
#    print('Dentro do limite de velocidade!')