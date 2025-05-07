while True:
    num1 = int(input('Entre com o primeiro numero: '))
    num2 = int(input('Entre com o segundo numero: '))

    num3 = num1 + num2

    if num3 % 2 == 0:
        print(f'A soma dos numeros {num1} e {num2} é par.')
    else:
        print(f'A soma dos numeros {num1} e {num2} é ímpar.')

    continuar = int(input('Deseja continuar? [0] Não   [1] Sim  '))
    if continuar == 0:
        break
