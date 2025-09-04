# Printe somente as colunas pares da matriz

matriz = [[c for c in range(5)] for l in range(5)]

print(matriz)

for colunas in range(len(matriz[0])):
    if colunas % 2 == 0:
        for linhas in range(len(matriz)):
            print(f'Linha: {linhas}, Coluna: {colunas}, Valor: {matriz[linhas][colunas]}')
