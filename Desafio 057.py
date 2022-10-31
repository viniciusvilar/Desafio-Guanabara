sexo = input('Informe seu sexo [M/F]: ').strip().lower()
while sexo not in 'mf':
    sexo = input('Informe seu sexo [M/F]: ').strip().lower()
print('Programa finalizado!')