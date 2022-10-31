cidade = input('Digite o nome da cidade: ')
cidade = cidade.strip()
cidade = cidade.upper()
print("A cidade começa com o nome SANTO? {}".format('SANTO'in cidade[0:5]))