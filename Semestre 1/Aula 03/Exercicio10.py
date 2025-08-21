# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$0.50 por km para viagen de até 200km, e R$0.45 para viagens mais longas.

dist = float(input('Insira a distância que deseja percorrer em km: '))

if dist <= 200:
    calculo = dist * 0.50
    print(f'O preço da passagem vai ser de R${calculo}')

else:
    calculo = dist * 0.45
    print(f'O preço da passagem vai ser de R${calculo}')
