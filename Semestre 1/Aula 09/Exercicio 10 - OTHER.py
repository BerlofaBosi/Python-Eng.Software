num = int(input('Insira um numero n: '))

for a in range(num):
    for b in range(num, 0, -1):
        if a + b == num:
            print(f'{a} + {b} = {num}')
