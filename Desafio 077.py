palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
for c in range(len(palavras)):
    analisador = palavras[c]
    print('Na palavra *{}* temos '.format(analisador), end=' ')
    for flag in analisador:
        if flag in 'aeiou':
            print(flag, end=' ')
    print()

