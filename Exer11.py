
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))


soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

# Evitar divisão por zero
if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Indefinida (não é possível dividir por zero)"


print("\n--- Resultados ---")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")


# Heverton Xavier