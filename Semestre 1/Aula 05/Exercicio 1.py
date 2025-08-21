num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

print('''Escolha sua operação: 
[1] +  
[2] -  
[3] *  
[4] /''')

operacao = int(input('Insira sua escolha: '))

if operacao == 1:
    print(f'A soma dos números inputados é: {num1 + num2}')

elif operacao == 2:
    print(f'A subtração dos números inputados é: {num1 - num2}')

elif operacao == 3:
    print(f'A multiplicação dos números inputados é: {num1 * num2}')

elif operacao == 4:
    print(f'A divisão dos números inputados é: {num1 / num2}')

else:
    print('Opção Inválida.')

