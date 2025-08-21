divs = 0
cont = x = int(input('Insira um número: '))

while cont > 0:
    if (x % cont) == 0:
        divs += 1

    cont -= 1

    if divs > 2:
        primo = False
        break

    primo = True

print(f'O número informado é primo? {primo}')
