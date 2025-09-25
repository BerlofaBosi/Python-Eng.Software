# Formas de criar o conjunto

a = set()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.remove(4)
# clear(a) -> Remove todos os elementos
print(a)

b = {1, 2, 3}
print(b)

lista = [1, 2, 3, 4, 5, 6, 7]
c = set(lista)

# Diferença
c = a - b
print(c)

# União
d = a | b
print(d)

# Intersecção
e = a & b
print(e)

# Diferença Simétrica (elementos que não estão repetidos)
f = a ^ b
print(f)
