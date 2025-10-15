l = [3, 15, 8, 9, 1]

def busca(l, c):
    for i in range(len(l)):
        if l[i] == c:
            return i

    return -1

print(busca(l, 15))

