from calculos2 import *
from calculos1 import *

while True:
    print('---'*20)
    print('(1) Soma; (2) Subtração; (3) Multiplicação; (4) Divisão; (5) Sair')
    op = int(input('Escolha sua opção: '))

    user1 = float(input('Insira o primeiro valor: '))
    user2 = float(input('Insira o segundo valor: '))

    print('\nResultado: ', end='')

    match op:
        case 1:
            print(soma(user1, user2))

        case 2:
            print(subtracao(user1, user2))

        case 3:
            print(multiplicacao(user1, user2))

        case 4:
            print(divisao(user1, user2))

        case 5:
            break

        case _:
            print('Opção Inválida')

