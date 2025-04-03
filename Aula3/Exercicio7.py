# Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80 km/h

velocidade = int(input('Insira a velocidade em que você estava com o carro: '))

if velocidade > 80:
    valorMulta = (velocidade - 80) * 5
    print(f'Infelizmente você foi multado! O valor da multa é de R${valorMulta}')

else:
    print('Fica em paz! Você não foi multado.')

