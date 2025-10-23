# O que é recursao? É um procedimento ou função que se chama.
# Ex: Floco de neve de Koch / Sequencia de Mandelbrot

# Meu jeito:
def soma(lista, contagem):
    if contagem == len(lista)-1:
        return 0
    contagem += 1
    return lista[contagem] + soma(lista, contagem)

l = [1,3,5,7,9]
print(soma(l, -1))

# Jeito do professor:
def somaLista(l):
    if len(l) == 1:
        return l[0]
    return l[0] + somaLista(l[1:])

l = [1,3,5,7,9]
print(somaLista(l))
