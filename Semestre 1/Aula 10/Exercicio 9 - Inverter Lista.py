# 9. Inverta uma lista usando um for.

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []

for i in range(len(lista1), 0, -1):
    lista2.append(lista1[i - 1])

print(lista1)
print(lista2)
