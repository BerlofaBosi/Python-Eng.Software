# Tupla é uma lista imutavel
a = (10, 24, 'Texto', True)

# É possivel escrever uma tupla omitindo os parenteses
b = 10, 24, 'Texto', True

# Tupla de um unico elemento. Precisa de ter a virgula para ser entendida como tupla!
c = (10,)

# Tupla de um unico elemento omitindo os parenteses.
d = 10,

# É possivel alterar o valor de um elemento de uma lista dentro de uma tupla.
e = (10, 9, 8, [1, 2])
e[-1][0] = 0

# É possivel atribuir valor a duas variavies em uma unica sentença atraves de uma tupla.
x, y = (1, 2)
print(x)
print(y)

nome, sobrenome = input('Digite seu nome e sobrenome: ').split()
print(nome)
print(sobrenome)


teste = [1, 40, 4.5, 3.4, 9]
for i, j in enumerate(teste):
    print(f'Index {i} : Valor {j}')
