entrada = 1234

a = entrada % 10
b = (entrada % 100) // 10
c = (entrada % 1000) // 100
d = (entrada % 10000) // 1000

calculo = a * b * c * d

print(calculo)
