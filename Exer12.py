
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3) / 3


print(f"\nA média das notas é: {media:.2f}")


if media >= 7:
    print("O aluno foi aprovado!")
else:
    print("O aluno foi reprovado!")


    # Heverton Xavier