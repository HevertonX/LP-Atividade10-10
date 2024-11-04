
salario = float(input("Digite o valor do salário: R$ "))
percentual_aumento = float(input("Digite o percentual de aumento: "))


aumento = salario * (percentual_aumento / 100)


novo_salario = salario + aumento


print(f"\nO novo salário, após um aumento de {percentual_aumento}% é: R$ {novo_salario:.2f}")


# Heverton Xavier