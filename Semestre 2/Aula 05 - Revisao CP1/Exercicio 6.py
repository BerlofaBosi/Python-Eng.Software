# Matriz Transposta

matriz = [[c for c in range(5)] for l in range(5)]

matrizTransposta = []

for colunas in range(len(matriz[0])):
    linha = []
    for linhas in range(len(matriz)):
        linha.append(matriz[linhas][colunas])

    matrizTransposta.append(linha)

print(matrizTransposta)
