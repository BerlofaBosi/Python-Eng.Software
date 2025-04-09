limite = 100

velocidade = float(input('Insira a velocidade em que você estava: '))

if velocidade > limite * 1.15:
    if velocidade <= 115:
        valorMulta = 100

    elif velocidade <= limite * 1.35:
        valorMulta = 200

    elif velocidade <= limite * 1.80:
        valorMulta = 500

    else:
        valorMulta = 1000

    print('Você foi multado!  Escolha a forma de pagamento:')
    formaPagamento = input('Débito [D]  Crédito [C] ').upper()

    if formaPagamento == 'D':
        valorMulta -= valorMulta * 0.1

    elif formaPagamento == 'C':
        valorMulta += valorMulta * 0.15

    print(f'O valor da multa, nesta modalidade de pagamento, será de R${valorMulta}')

else:
    print('Fica em paz! Você está dentro do limite de velocidade.')