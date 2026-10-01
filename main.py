import numpy as np
import matplotlib.pyplot as plt

opcoes = {
    "1": 0 + 0j,
    "2": 0.3 + 0.5j,
    "3": 1 + 0j,
    "4": -1 + 0j,
    "5": -0.5 + 0.5j
}

print("Escolha um número complexo:")
print("1 - 0 + 0j")
print("2 - 0.3 + 0.5j")
print("3 - 1 + 0j")
print("4 - -1 + 0j")
print("5 - -0.5 + 0.5j")
print("6 - Digitar um número próprio")

escolha = input("\nEscolha uma opção: ")

if escolha in opcoes:
    c_escolhido = opcoes[escolha]
else:
    real = float(input("Digite a parte real: "))
    imaginario = float(input("Digite a parte imaginária: "))
    c_escolhido = complex(real, imaginario)

largura = 1000
altura = 1000
max_iteracoes = 100

real = np.linspace(-2, 1, largura)
imaginario = np.linspace(-1.5, 1.5, altura)

imagem = np.zeros((altura, largura))

for y in range(altura):
    for x in range(largura):
        c = real[x] + imaginario[y] * 1j
        z = 0

        for i in range(max_iteracoes):
            z = z**2 + c

            if abs(z) > 2:
                break

        imagem[y, x] = i

plt.figure(figsize=(10, 10))

plt.imshow(
    imagem,
    extent=[-2, 1, -1.5, 1.5],
    cmap="inferno"
)

plt.scatter(
    c_escolhido.real,
    c_escolhido.imag,
    color="cyan",
    s=50,
    label=f"c = {c_escolhido}"
)

plt.xlabel("Parte real")
plt.ylabel("Parte imaginária")
plt.title("Conjunto de Mandelbrot")

plt.legend()
plt.axis("equal")
plt.show()