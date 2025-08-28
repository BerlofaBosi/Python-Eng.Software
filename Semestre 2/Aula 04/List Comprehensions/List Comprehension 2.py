from math import sin
import mult

angulos = [3.14, 0, 1.72, 2*3.14]

senos = [sin(i) for i in angulos] # Calcula o seno de todos os itens da lista
print(senos)


l5 = [mult.multiplicacao(i, i) for i in angulos]
print(l5)