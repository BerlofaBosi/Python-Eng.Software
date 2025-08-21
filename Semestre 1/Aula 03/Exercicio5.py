# Faça um programa que solicite o preço de uma mercadoria e o percental de desconto.
# Exiba o valor do desconto e o preço a pagar.

precoProduto = float(input('Insira o preço do produto que deseja comprar: '))
percentual = float(input('Insira o percentual de desconto do produto: '))

precoFinal = precoProduto - (percentual/100 * precoProduto)

print(f'O valor de R${precoProduto:.2f} com o desconto de {percentual}% será de R${precoFinal:.2f}')
