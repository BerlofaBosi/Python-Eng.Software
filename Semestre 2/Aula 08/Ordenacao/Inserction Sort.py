lista = [58, 18, 5, 4, 6]
print(lista)

for j in range(1, len(lista)):
    aux = lista[j]

    while j > 0 and aux < lista[j-1]:
        lista[j] = lista[j-1]
        j = j-1

    lista[j] = aux
    print(lista)
