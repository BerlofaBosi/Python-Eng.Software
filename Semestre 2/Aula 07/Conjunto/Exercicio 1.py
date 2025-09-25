# Escreva um programa que compare duas listas. Utilizando operações de conjuntos, imprima:
# 1) Os valores comum às duas listas
# 2) Os valores que só existem na primeira
# 3) Os valores que existem apenas na segunda
# 4) Uma lista com os elementos não repetidos das duas listas (^)

valComum = lambda l1, l2: set(l1) & set(l2)
valPrimeira = lambda l1, l2: set(l1) - set(l2)
valSegunda = lambda l1, l2: set(l2) - set(l1)
valNaoRepetidos = lambda l1, l2: set(l1) ^ set(l2)

a = [1, 2, 5, 7]
b = [5, 7, 9, 10]

print(f'Valor Comum: {valComum(a, b)}')

print(f'Valores que só existem na primeira: {valPrimeira(a, b)}')

print(f'Valores que só existem na segunda: {valSegunda(a, b)}')

print(f'Elementos não repetidos das duas listas: {valNaoRepetidos(a, b)}')
