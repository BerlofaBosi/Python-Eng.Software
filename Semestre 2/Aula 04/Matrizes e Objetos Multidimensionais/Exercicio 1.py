# Crie uma matriz de dimensões l x c e atribuindo valor zero para todos os elementos
# (peça ao usuário o tamanho da matriz)

l = int(input('linhas: '))
c = int(input('colunas: '))

matriz = []

for a in range(l):
    linha = []
    for b in range(c):
        linha.append(0)
    matriz.append(linha)
print(matriz)


matriz2 = [[0 for a in range(c)] for i in range(l)]
print(matriz2)