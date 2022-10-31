from modulos import mostrarMenu, valOp

'''
cadPessoa('Don Vito Corleone', 67)
cadPessoa('Michael Corleone', 34)
cadPessoa('Bruce Wayne', 30)
cadPessoa('Clark Kent', 100)
cadPessoa('Harry Potter', 11)
cadPessoa('Hermione Granger', 11)
cadPessoa('Rony Weasley', 11)
cadPessoa('Diana', 143)
cadPessoa('Barry Allen', 28)'''

while True:
    mostrarMenu()
    flag = valOp()
    if flag == 3:
        break
