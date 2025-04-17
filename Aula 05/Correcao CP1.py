print('Olá, seja muito bem vindo a Vinheria Agnello!')
print()
nome = input('Qual o seu nome?')
ender = input('Qual o seu endereço?')
ano = int(input('Qual seu ano de nascimento?'))
print()

idade = 2025 - ano

if idade >= 18:
    print('Os vinhos da casa são:')
    print('-------------------------------')
    print('1 - Vinho seco      --- R$37.50')
    print('2 - Vinho rosé      --- R$17.50')
    print('3 - Vinho suave     --- R$52.99')
    print('4 - Vinho branco    --- R$23.23')
    print('5 - Vinho bordeaux  --- R$87.40')
    print('-------------------------------')
    print()
    # ESCOLHA DO VINHO
    vinho = input('Escolha o número do vinho desejado:')
    qtde = int(input('Escolha quantas garrafas você deseja:'))
    if vinho == '1':
        preco = 37.50
    if vinho == '2':
        preco = 17.50
    if vinho == '3':
        preco = 52.99
    if vinho == '4':
        preco = 23.23
    if vinho == '5':
        preco = 87.40

    valor = preco*qtde
    print(f'O valor é de R${valor}')
    # FRETE
    if valor >= 150:
        frete = 0
        print('Você tem isenção no frete.')
    else:
        frete = 10
        print(f'O frete é de R${frete}')
    valor_2 = valor + frete
    print(f'O valor da sua compra com o frete é de R${valor_2}')
    # IDOSO
    if idade >= 60:
        print('Você possui um desconto de 5%!')
        vf = valor_2*0.95
    else:
        vf = valor_2

    print(f'{nome} a sua compra foi de R${vf})
    print(f'Será entregue no endereço {ender}')
    print(f'Obrigado pela compra, sr/a {nome}. O valor total foi de {vf} e será entregue no endereço {ender}')
else:
    print('Você é menor de idade, volte mais tarde!')
