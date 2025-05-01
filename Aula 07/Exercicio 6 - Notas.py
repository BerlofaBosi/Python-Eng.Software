notas = []


def media(_lista):
    soma = 0
    for c in range(0, len(_lista)):
        soma += _lista[c]
    return soma / len(_lista)


while True:
    inputNota = float(input('Insira a nota: (-1 para sair) '))

    if inputNota == -1:
        break

    notas.append(inputNota)


print(f'A média de todas as notas inputadas é: {media(notas)}')
