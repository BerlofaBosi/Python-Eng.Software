objeto = [
    [1, 2, 3], # Linha 1
    1,         # Linha 2
    [0, 2]     # Linha 3
]

# Matriz todas as linhas são do mesmo tamanho.

matriz = [
    [3, 0, 3], # Linha 1
    [7, 1, 0], # Linha 2
    [9, 1, 3]  # Linha 3
]


lin = 3
col = 4
matriz = []
for j in range(lin):
    linha = []
    for i in range(col):
        linha.append(int(input('Digite um valor: ')))
    matriz.append(linha)

print(matriz)