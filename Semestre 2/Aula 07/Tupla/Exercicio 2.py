# Crie uma maneira para remover elementos em uma tupla

def removeTupla(tupla, elemento):
    lista = list(tupla)
    for i, j in enumerate(lista):
        if j == elemento:
            lista.pop(i)
    return tuple(lista)


a = (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
print(a)
print(removeTupla(a, 3))
