# Escreva um programa que pergunte a quantidade de km percorridos por um
# carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

distPerc = float(input('Insira a quantidade de Km percorridos pelo carro: '))
dias = int(input('Insira quantos dias você ficou com o carro: '))

calculo = (distPerc * 0.15) + (dias * 60)

print(f'Após rodar {distPerc}km por {dias} dias, o preço a se pago é de R${calculo:.2f}')
