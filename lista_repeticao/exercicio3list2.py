"""
Para fazer o balanço mensal de um armazém, faça um programa que que leia para um
número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a
quantidade vendida. A partir desses dados imprima: o número total de mercadorias
diferentes lidas, o faturamento total e o lucro total do armazém. 
"""
total_mer_dif = int(input("Digite o valor total de mercadorias diferentes: "))
faturamento_total = 0
lucro_total = 0


for i in range(total_mer_dif):
    v_custo = float(input("Digite o valor de custo da mercadoria: R$"))
    v_prod = float(input("Digite o valor de venda da mercadoria: R$"))
    n_prod_v = int(input("Digite a quantidade de mercadoria vendida: "))
    lucro_ppdt = (v_prod - v_custo) * n_prod_v
    faturamento_total = faturamento_total + v_prod*n_prod_v
    lucro_total = lucro_total + lucro_ppdt

margem_l = (lucro_total/faturamento_total)*100

print(f"O número total de mercadorias diferentes lida foi: {total_mer_dif}")
print(f"O faturamento total deste armazém foi de R${faturamento_total}")
print(f"O lucro total deste armazém foi de R${lucro_total}")
print(f"E sua margem de lucro é igual a {margem_l:.0f}%")

print("Fim do programa")
    
