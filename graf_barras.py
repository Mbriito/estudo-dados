import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

title = "Grafico de Barras"
eixox = "EixoX"
eixoy = "EixoY"


# Titulo#Eixos
plt.title("Grafico de Barras")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x, y)
plt.show()
