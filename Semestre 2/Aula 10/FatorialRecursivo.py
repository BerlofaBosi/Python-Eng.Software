def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

print(fatorial(4))

def loop(n):
    fatorial = n
    while True:
        n -= 1
        if n == 0:
            break
        fatorial = fatorial * n
    return fatorial

print(loop(4))
