def busca_binaria(l, c):
    inicial = 0
    final = len(l) - 1

    while inicial <= final:
        meio = (final + inicial) // 2

        if c == l[meio]:
            return meio

        elif c > l[meio]:
            inicial = meio + 1

        elif c < l[meio]:
            final = meio - 1

    return -1

l = [12, 25, 37, 38, 41, 53, 59, 68, 71, 95]
print(busca_binaria(l, 53))
