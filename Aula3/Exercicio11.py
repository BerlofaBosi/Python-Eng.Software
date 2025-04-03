# Vamos escrever um programa que lê um número e verifica em qual dos seguintes casos o número se enquadra:
# Par e menor que 100
# Par e maior ou igual a 100
# Impar e menor que 100
# Impar e maior ou igual a 100
# a. Usando apenas operadores lógicos
# b. Usando apenas operadores relacionais

num = int(input('Insira um número: '))

print('\nOperadores Lógicos: \n')

print('Par e menor que 100? ', num % 2 == 0 and num < 100)
print('Par e maior ou igual a 100? ', num % 2 == 0 and num >= 100)
print('Impar e menor que 100? ', num % 2 != 0 and num < 100)
print('Impar e maior ou igual a 100? ', num % 2 != 0 and num >= 100)

print('\nOperadores Relacionais: \n')

if num % 2 == 0 and num < 100:
    print('O número é par e menor que 100.')

if num % 2 == 0 and num >= 100:
    print('O número é par e maior que 100.')

if num % 2 != 0 and num < 100:
    print('O número é impar e menor que 100.')

if num % 2 != 0 and num >= 100:
    print('O número é impa e maior que 100.')
