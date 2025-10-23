import matplotlib.pyplot as plt
# Coordenadas x e y
x = [i for i in range(-100, 100)]
y = [i**2 for i in x]

# Plotando o gráfico
plt.plot(x, y, marker='o', linestyle='-')  # marker='o' para usar círculos, linestyle='-' para usar uma

plt.title('Gráfico de Coordenadas x, y')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)  # Adiciona uma grade ao gráfico
plt.show()
