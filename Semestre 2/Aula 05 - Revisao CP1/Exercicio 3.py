# Printe somente a diagonal da matriz

matriz = [[c for c in range(5)] for l in range(5)]

for linhas in range(len(matriz)):
    for colunas in range(len(matriz[linhas])):
        if linhas == colunas:
            print(f'Linha: {linhas}, Coluna: {colunas}, Valor: {matriz[linhas][colunas]}')
