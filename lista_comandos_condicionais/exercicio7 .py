"""
Um microempresário tem por norma retirar mensalmente 40% do lucro de sua
empresa para os seus gastos pessoais se o lucro ultrapassar R$ 3.000,00 e retirar
apenas R$ 1.000,00 se o lucro for menor que isso. Faça um programa que leia do
teclado o faturamento mensal e o total das despesas para calcular o lucro (lucro =
faturamento - despesas) e imprima quanto o microempresário deve retirar neste mês.
Declare com constantes simbólicas o lucro mínimo, a retirada mínima e o limite da
retirada.
"""
# Constantes simbólicas
lucro_MIN = 3000.00
ret_MIN = 1000.00
val_porcen = 0.4

# Entrada das informações/variaveis
fat_mensal = float(input("Digite o valor do faturamento mensal: R$"))
desp_mensal = float(input("Digite o valor da despesa mensal: R$"))

#função/corpo da função
lucro = fat_mensal - desp_mensal

retirada = lucro * 0.4

#resultados
if lucro > 3000:
    print(f"O lucro da empresa este mês foi de R${lucro}")
    print(f"O microempresário deve retirar R${retirada} este mês")
else:
    print(f"O lucro da empresta este mês foi de R${lucro}")
    print(f"O microempresário deve retirar R${retirada} este mês")
