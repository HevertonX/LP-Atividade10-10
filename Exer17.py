
deposito = float(input("Digite o valor do depósito bancário: R$ "))
taxa_juros_anual = float(input("Digite a taxa de juros anual (em %): "))


taxa_juros_decimal = taxa_juros_anual / 100


valor_1_ano = deposito * (1 + taxa_juros_decimal) ** 1
valor_5_anos = deposito * (1 + taxa_juros_decimal) ** 5
valor_10_anos = deposito * (1 + taxa_juros_decimal) ** 10


print(f"\nO valor acumulado após 1 ano é: R$ {valor_1_ano:.2f}")
print(f"O valor acumulado após 5 anos é: R$ {valor_5_anos:.2f}")
print(f"O valor acumulado após 10 anos é: R$ {valor_10_anos:.2f}")


# Heverton Xavier