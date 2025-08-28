# Sintaxe: list = [expression for item in iterable if condition == True]

l1 = []
for i in range(10):
    if i >= 5:
        lista1.append(i*2)
print(l1)


l2 = [i*2 for i in range(10) if i >= 5] # Dobro dos itens da lista
print(l2)


notas = [10, 8, 7, 4, 6]

l3 = [i**2 for i in notas] # Ao quadrado dos itens da lista
print(l3)

l4 = [i for i in notas if i >= 6] # Filtro de 6 pra cima

l5 = [i for i in range(1, 100) if i % 2 == 0] # Pares
l6 = [i for i in range(1, 100) if i % 2 == 0] # Impares

