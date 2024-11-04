
preco_produto = float(input("Informe o preço do produto: "))
desconto = float(input("Informe o porcentual do disconto: "))


valor_final = preco_produto * (1 - (desconto / 100))


print(f"O valor final do produto junto com o desconto é: R$ {valor_final:.2f}")


# Heverton Xavier