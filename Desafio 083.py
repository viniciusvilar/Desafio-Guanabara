exp = input('Digite a expressão: ')
contParenAber = 0
contParenFech = 0
for c in exp:
    if c == '(':
        contParenAber += 1
    elif c == ')':
        contParenFech += 1
if contParenAber == contParenFech:
    print('Expressão Valida!')
else:
    print('Expressão inválida!')

