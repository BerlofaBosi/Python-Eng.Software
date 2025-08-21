# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários sueriores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, de 15%

salario = float(input('Insira o salário: '))

if salario > 1250:
    aumento = 1250 * 0.1
    print(f'O valor do aumento é de R${aumento:.2f}. Com isso, o novo salário será de R${salario+aumento:.2f}')

if salario <= 1250:
    aumento = 1250 * 0.15
    print(f'O valor do aumento é de R${aumento:.2f}. Com isso, o novo salário será de R${salario+aumento:.2f}')
