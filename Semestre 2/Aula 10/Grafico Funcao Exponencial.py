import matplotlib.pyplot as plt

def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

def expo(a, n):
    if n == 0:
        return 1
    return a * expo(a, n-1)

def somatoria(x, n):
    if n == 0:
        return 1
    return expo(x, n) / fatorial(n) + somatoria(x, n-1)

print(somatoria(2, 100))

x = [i/100 for i in range(1000)]
y = [somatoria(i, 100) for i in x]

plt.plot(x, y, marker='o', linestyle='-')
plt.title('Gráfico de Coordenadas x, y')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.show()