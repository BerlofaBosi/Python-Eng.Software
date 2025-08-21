def printa(*args):
    txt = ''
    for i in args:
        txt += str(i) + ' '

    return txt[:-1]


print(printa(10, 'ola', 'oi', 'fiap', 10))

def med(*args):
    soma = 0
    for i in args:
        soma += i

    return soma/len(args)

a = [10, 10.34, 9, 1]
print(med(*a)) # *a -> a[0], a[1], a[2], a[3]

