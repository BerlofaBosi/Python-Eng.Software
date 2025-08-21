# 10.Verifique se um número existe em uma lista.

lista = [10, 20, 40, 1923, 12039213]
verificado = False

user = int(input('Insira o numero a ser verificado: '))

for i in range(len(lista)):
    if lista[i] == user:
        verificado = True

print('O numero digitao está na lista? ', verificado)

#if user in lista:
#    print('O número esta na lista!')
#else:
#    print('O número não está na lista.')
