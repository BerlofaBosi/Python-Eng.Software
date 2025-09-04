# Calcule a soma de cada linha da matriz

matriz = [[c for c in range(5)] for l in range(5)]

for linhas in range(len(matriz)):
    soma = 0
    for colunas in range(len(matriz[linhas])):
        soma += matriz[linhas][colunas]

    print(f'Linha: {linhas}, Soma: {soma}')
