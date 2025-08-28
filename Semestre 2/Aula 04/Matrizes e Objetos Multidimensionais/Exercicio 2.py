# Crie uma matriz de dimensões l x c e atribua os valores de 1 até 1 x c para os elementos da matriz.
# Exemplo: matriz 3x2: [[1,2], [3,4], [5,6]]

l = int(input('linhas: '))
c = int(input('colunas: '))

matriz = []

for a in range(l):
    linha = []
    for b in range(c):
        linha.append((b + 1) + a * c)
    matriz.append(linha)
print(matriz)
