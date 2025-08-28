# Converta uma lista de temperaturas em Celsius [0, 10, 20, 30, 40] para Fahrenheit
# usando a fórmula F = C * 9/5 + 32

celsius = [0, 10, 20, 30, 40]
convert = lambda x : x * 9/5 +32
fahrenheit = [i * 9/5 +32 for i in celsius]

print(fahrenheit)
