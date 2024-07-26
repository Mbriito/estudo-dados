import matplotlib.pyplot as plt
x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
Z = [20, 25, 400, 3000, 100]

titulo = "Scatterplot: grafico de dispersao"
eixox = "Eixo X"
eixoy = "Eixo Y"


# Legenda
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color="r", linestyle="--")
plt.scatter(x, y, label="Meus pontos", color="#FF1493", marker=".", s=100)
plt.plot(x, y)
plt.legend()
#plt.show()
plt.savefig("fig1.png", dpi=300)
