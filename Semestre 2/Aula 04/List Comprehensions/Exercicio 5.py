# Gere uma lista com os números de 1 a 20, substituindo os múltiplos de 3 por "Fizz"

l = ['Fizz' if i % 3 == 0 else i for i in range(1, 21)]

print(l)
