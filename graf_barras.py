import matplotlib.pyplot as plt
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]


title = "Grafico de Barras2"
eixox = "EixoX"
eixoy = "EixoY"


# Legenda
plt.title(title)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x1, y1, label = "Grupo1")
plt.bar(x2, y2, label = "Grupo2")
plt.legend()

plt.show()
