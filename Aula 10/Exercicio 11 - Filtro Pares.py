# 11.Filtre uma lista e crie outra com apenas os números pares.

listaImpar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaPar = []
indexs = []

print(listaImpar)

for i in range(len(listaImpar)):
    if listaImpar[i] % 2 == 0:
        listaPar.append(listaImpar[i])
        indexs.append(i)

for i in range(len(indexs), 0, -1):
    listaImpar.pop(indexs[i - 1])

print('Impar: ', listaImpar)
print('Par: ', listaPar)
