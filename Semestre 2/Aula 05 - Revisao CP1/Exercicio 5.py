# Calcule a soma de cada coluna da matriz

matriz = [[c for c in range(5)] for l in range(5)]

for colunas in range(len(matriz[0])):
    soma = 0
    for linhas in range(len(matriz)):
        soma += matriz[linhas][colunas]

    print(f'Coluna: {colunas}, Soma: {soma}')
