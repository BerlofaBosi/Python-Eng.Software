num = int(input('Insira o numero a ser verificado: '))

divs = 0

for i in range(num+1, 1, -1):
    if num % i == 0:
        divs += 1

    if divs > 2:
        primo = False
        break

    primo = True

print(f'É primo? {primo}')
