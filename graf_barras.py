import matplotlib.pyplot as plt
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]


title = "Grafico de Barras"
eixox = "EixoX"
eixoy = "EixoY"


# Titulo#Eixos
plt.title("Grafico de Barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x1, y1)
plt.bar(x2, y2)
plt.show()
