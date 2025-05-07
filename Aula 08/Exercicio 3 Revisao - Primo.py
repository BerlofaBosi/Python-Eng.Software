while True:
    divs = 0
    x = int(input('Insira um número: '))
    cont = x
    primo = False

    while cont > 0:
        if (x % cont) == 0:
            divs += 1

        cont -= 1

        if divs > 2:
            primo = False
            break
        else:
            primo = True

    print(f'O número informado é primo? {primo}')

    continuar = int(input('Deseja continuar? [0] Não   [1] Sim  '))
    if continuar == 0:
        break
