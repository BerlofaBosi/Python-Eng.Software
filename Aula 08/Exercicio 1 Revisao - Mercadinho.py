preco = 0

while True:
    print("""
Codigo     Preço R$
    0       Terminar a compra.
    1       0.50
    2       1,00
    3       4,00
    4       7,00
    5       8,00
""")

    escolha = int(input('Insira o codigo do produto desejado: '))

    if escolha == 0:
        break

    match escolha:
        case 1:
            preco += 0.5
        case 2:
            preco += 1.0
        case 3:
            preco += 4.0
        case 4:
            preco += 7.0
        case 5:
            preco += 8.0
        case _:
            print('Este produto não existe.')

    print('---'*30)
    print(f'Total da compra até agora: R${preco}')

print('---'*30)
print(f'O preço total da sua compra ficou de R${preco}')
