print('Determine um intervalo A e B.')
a = int(input('A: '))
b = int(input('B: '))

print('-'*30)

for i in range(a, b+1):
    if i % 2 == 0:
        print(i, end=' ')

print('-'*30)
