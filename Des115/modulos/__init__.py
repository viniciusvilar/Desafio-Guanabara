from time import sleep

def mostrarMenu(menu=0):
    if menu == 0:
        print('='*35)
        print('MENU PRINCIPAL'.center(32))
        print('='*35)
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar pessoa')
        print('3 - Sair do sistema')
        print('=' * 35)
    elif menu == 1:
        print('=' * 35)
        print('PESSOAS CADASTRADAS'.center(32))
        print('=' * 35)
    elif menu == 2:
        print('=' * 35)
        print('CADASTRAR PESSOA'.center(32))
        print('=' * 35)
    else:
        print('=' * 35)
        print('SAINDO DO SISTEMA!'.center(32))
        print('=' * 35)


def valOp():
    op = 0
    while True:
        try:
            op = int(input("Opção: "))
        except (ValueError):
            print('Erro! Digite um valor INTEIRO VÁLIDO válido')
            continue
        except (KeyboardInterrupt):
            print('O usuário interrompeu o programa!')
            mostrarMenu(3)
            op = 3
            break
        else:
            if (op <= 0) or (op >= 4):
                print('OPÇÃO INEXISTENTE! Tente novamente')
                sleep(0.5)
                mostrarMenu()
            elif op == 1:
                conPessoa()
                sleep(0.5)
                mostrarMenu()
            elif op == 2:
                cadPessoa()
                sleep(0.5)
                mostrarMenu()
            elif op == 3:
                mostrarMenu(3)
                break
            else:
                break
    return op


def valIdade():
    idade = 0
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('Idade INVÁLIDA! Digite apenas números!')
            continue
        else:
            break
    return idade


def conPessoa():
    arquivo = open('listaCadastrados.txt', 'r')
    listaPessoas = list()
    for linha in arquivo:
        linha.strip().split()
        listaPessoas.append(linha.replace('\n', ''))
    arquivo.close()
    mostrarMenu(1)
    for c in range(len(listaPessoas)):
        if c % 2 == 0:
            print('{:<20}'.format(listaPessoas[c]), end='')
        else:
            print('{:>10} anos'.format(listaPessoas[c]))
    #return listaPessoas[:]



def cadPessoa():
    mostrarMenu(2)
    nome = input('Nome: ')
    idade = valIdade()
    arquivo = open('ListaCadastrados.txt', 'a')
    print('Novo registro de {} adicionado.'.format(nome))
    arquivo.write('{}\n'.format(nome))
    arquivo.write('{}\n'.format(idade))
    arquivo.close()
