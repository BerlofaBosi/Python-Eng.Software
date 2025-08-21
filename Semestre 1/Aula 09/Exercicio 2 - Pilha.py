fila = []

while True:
    x = int(input('Você deseja inserir ou atender uma pessoa? [0] inserir  [1] atender '))

    match x:
        case 0:
            fila.append(input('Insira o nome da proxima pessoa a ser atendida: '))
        case 1:
            fila.pop(len(fila)-1)
        case _:
            break

    print('-'*50)
    print(fila)
    print('-'*50)
