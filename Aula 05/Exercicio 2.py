x = float(input('Insira o valor de X: '))

if x < 2:
    y = x

elif x <= 3.5:
    y = 2

elif x < 5:
    y = 3

else:
    y = x ** 2 - 10 * x + 28

print(f'Dado x={x}, teremos y={y}')
