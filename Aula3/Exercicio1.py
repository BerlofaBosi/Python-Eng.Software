# Escreva um programa que retorne se o cliente pode ou não contratar um empréstimo
# (com base em duas condições, idade e salário).
# O programa deve escrever na tela True ou False.

salario = float(input('Entre com o salário: '))
idade = int(input('Entre com a sua idade: '))
indicacao = bool(input('Você tem uma indicação? SIM(1) NÃO(0) '))

print('Você pode pegar um empréstimo: ', (idade >= 18 and salario >= 3000) or indicacao)
