# 4. Encontre o maior número em uma lista.

lista = [10, 20, 40, 1923, 12039213]
maior = 0

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]

print(lista)
print('O maior numero na lista é: ', maior)
