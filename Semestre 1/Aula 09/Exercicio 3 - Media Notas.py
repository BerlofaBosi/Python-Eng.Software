notas = [10, 9, 7, 5, 3, 4]

media = 0

for i in range(len(notas)):
    media += notas[i]
    print(notas[i])

media /= len(notas)

print(f'A media das notas é: {media:.2f}')
