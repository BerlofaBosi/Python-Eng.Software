num = int(input('Insira um numero n: '))

a = []
b = []

for i in range(num-1, 0, -1):
    a.append(f'{i:0>2d}')

for i in range(1, num):
    b.append(f'{i:0>2d}')

for i in range(len(a)):
    print(f'{a[i]} + {b[i]} = {num}')
