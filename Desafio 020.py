import random
alu0 = input("Primeiro aluno: ")
alu1 = input('Segundo aluno: ')
alu2 = input('Terceiro aluno: ')
alu3 = input('Quarto aluno: ')
alunos = [alu0, alu1, alu2, alu3]
random.shuffle(alunos)
print('A ordem de apresentação será:')
print(alunos)