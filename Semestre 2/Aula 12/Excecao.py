a = input('Digite um valor: ')

try:
    b = float(a)
    print(b)

except ValueError:
    print('Valor digitado não é válido.')

except ZeroDivisionError:
    print('Divisão por zero não é possível.')

#except (ZeroDivisionError, ValueError):
#   print('Valor digitado inválido ou divisão por zero.')

else:
    print('Será executado quando não tiver exceção!')

finally:
    print('Sempre será executado!')

