numerosExtenso = ('Zero', 'Um', 'Dois','Três','Quatro','Cinco','Seis','Sete','Oito'
                  ,'Nove','Dez','Onze','Doze','Treze','Catorze','Quize','Dezesseis','Dezessete',
                  'Dezoito'
                  ,'Dezenove', 'Vinte')
numero = int(input('Digite um número entre 0 e 20: '))
while numero < 0 or numero > 20:
    numero = int(input('Tente novamente! Digite um número entre 0 e 20: '))
print('Você digitou o número {}'.format(numerosExtenso[numero]))