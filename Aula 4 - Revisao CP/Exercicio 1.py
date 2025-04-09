codigoMercadoria = input('Insira o código da mercadoria: ')
precoMercadoria = float(input('Insira o preço dessa mercadoria: '))

if codigoMercadoria == '00':
    precoMercadoria -= precoMercadoria * 0.1 #Desconto de 10%

elif codigoMercadoria == 'AA'
    precoMercadoria -= precoMercadoria * 0.15 #Desconto de 15%

elif codigoMercadoria == 'CC'
    precoMercadoria -= precoMercadoria * 0.35 #Desconto de 35%

print(f'O preço final do produto será de R${precoMercadoria:.2f}')
