# 7. Conte quantos números pares existem em uma lista.

lista = [10, 20, 40, 1923, 12039213]
pares = 0

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares += 1

print(lista)
print(f'Existem {pares} numeros pares na lista.')
