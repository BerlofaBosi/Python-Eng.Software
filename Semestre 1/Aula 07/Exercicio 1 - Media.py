soma = 0
qnt = 0

while True:
    x = int(input('Insira um valor ou 0 para sair: '))
    soma += x

    if x == 0:
        break

    qnt += 1

print(f'A soma é {soma} e a média é {soma / qnt}.')
