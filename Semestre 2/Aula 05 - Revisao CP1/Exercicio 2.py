# Printe somente as linhas impares da matriz

matriz = [[c for c in range(10)] for l in range(5)]

print(matriz)

for linhas in range(len(matriz)):
    if linhas % 2 != 0:
        for colunas in range(len(matriz[linhas])):
            print(f'Linha: {linhas}, Coluna: {colunas}, Valor: {matriz[linhas][colunas]}')
