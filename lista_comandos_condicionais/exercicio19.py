"""
Uma empresa deseja fazer o reajuste salarial dos seus funcionários da seguinte
forma: se o empregado for da categoria “Técnico”, receberá 30% de aumento, se for
da categoria “Gerente”, receberá 20% de aumento e os demais funcionários
receberão 15% de aumento. Faça um programa utilizando o comando if else aninhado
que leia do teclado o salário e a categoria do funcionário, calcule e imprima o seu
novo salário. 
"""

sal_atual = float(input("Digite o valor do salário atual: R$"))
categoria = input("Digite a sua categoria: ")


if categoria == "tecnico":
    novo_salario = sal_atual * 1.30
elif categoria == "gerente":
     novo_salario = sal_atual * 1.20
else:
      novo_salario = sal_atual * 1.15

print(f"O novo salário do funcionário é: R$ {novo_salario:.2f}")

print("FIM")