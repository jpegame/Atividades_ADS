"""
5. Em uma loja de eletroeletrônicos, um vendedor que consiga vender mais de R$
3.000,00 por mês recebe como comissão 5% do valor vendido. Abaixo disso, ele não
recebe nenhuma comissão. Faça um programa que leia do teclado o total de vendas
mensais de um vendedor e imprima se ele tem direito a comissão e, se tiver, de
quanto. 
"""
#Constante simbólicas
Limite_Vendas = 3000
Porcentual_Comissão = 5

#Declarei variáveis para o valor "total de vendas" e o cálculo da porcentagem da "comissão"
Total_Vendas = float(input("Indique o valor total de vendas mensais: R$"))
Valor_Comissão = Total_Vendas * (Porcentual_Comissão/100)

#Condição para receber comissão ou não
if Total_Vendas > 3000:
    print(f"O vendedor tem direito a uma comissão de R${Valor_Comissão:.2f}")
else:
    print("O vendedor não tem direito a comissão")