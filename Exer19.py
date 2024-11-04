
numero = int(input("Digite um número para ver a sua tabuada: "))

# Exibir a tabuada de 1 a ...
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")


# Heverton Xavier