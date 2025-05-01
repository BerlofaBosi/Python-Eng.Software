notas = [8.0, 5.5, 9.4, 7.6, 3.1, 0.5, 1.2, 9.8]
notas2 = [10, 9.4, 3.5]

print(notas)
print(notas[0])
print(notas[0:3])
print(len(notas))

notas.append(6.7) # Acrescenta um elemento no final da lista
print(notas)

notas.append(notas2) # Insere a lista dentro da outra lista
print(notas)

notas.extend(notas2) # Concatena uma lista a outra
print(notas)

notas.pop(9) # Remove o index inserido
print(notas)

la = [10, 20, 30]
lb = la # --> Nesse caso, você está apontando para a lista.
#             Caso queira copiar utilize la.copy() ou la[:]

la[0] = 13

print(la)
print(lb)