consumo = int(input('Insira a quantidade de kWh consumida: '))
tipoInstalacao = input('Selecione o tipo de instalação: Residêncial [R]  Industrial [I]  Comercial [C] ').upper()

if tipoInstalacao == 'R':
    if consumo <= 500:
        valor = consumo * 0.4
    else:
        valor = consumo * 0.65

elif tipoInstalacao == 'I':
    if consumo <= 1000:
        valor = consumo * 0.55
    else:
        valor = consumo * 0.60

elif tipoInstalacao == 'C':
    if consumo <= 5000:
        valor = consumo * 0.55
    else:
        valor = consumo * 0.60

print(f'Para o consumo de {consumo}kWh, no seu tipo de instalação, terá de ser pago R${valor:.2f}.')
