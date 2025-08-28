# Dada a lista de palavras ["maçã", "banana", "uva", "morango", "abacaxi"],
# crie uma nova lista contendo apenas as palavras com mais de 5 letras

palavras = ["maçã", "banana", "uva", "morango", "abacaxi"]

l = [i for i in palavras if len(i) > 5]

print(l)
