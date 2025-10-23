def combinatoria(m, n):
    if n == 0:
        return 1
    elif m == n:
        return 1
    elif m < n:
        return 0

    return combinatoria(m -1, n) + combinatoria(m-1, n-1)

print(combinatoria(5, 2))
