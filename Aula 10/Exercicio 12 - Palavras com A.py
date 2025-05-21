# 12.Dada uma lista de palavras, crie uma nova com as palavras que começam com a letra "a".

lista = ['Arthur', 'Davi', 'Danilo', 'Mateus']
listaA = []

for i in lista:
    if i[0] == 'A':
        listaA.append(i)

print(lista)
print(listaA)
