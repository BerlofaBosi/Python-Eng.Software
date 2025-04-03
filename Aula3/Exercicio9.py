# Escreva um programa que leia três números e que imprima o maior e menor.

lista = []

ordem = bool(input('Você quer uma lista crescente[0] ou decrescente[1]? '))

lista.append(int(input('Insira o 1º número: ')))
lista.append(int(input('Insira o 2º número: ')))
lista.append(int(input('Insira o 3º número: ')))

lista.sort(reverse=ordem)

for c in range(0, len(lista)):
    print(f'{c+1}º número: {lista[c]}')
