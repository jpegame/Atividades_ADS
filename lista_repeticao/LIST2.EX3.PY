total = int(input("Qual o N total de mercadorias vendidas?: "))
lucro_total = 0 
faturamento_total = 0

for i in range (total):
    p_custo = float(input("p.custo: "))
    p_venda = float(input("p_venda: "))
    q_vendida =int(input("q_vendida: "))
    lucro_p = (p_venda - p_custo)*q_vendida
    faturamento_total = faturamento_total + p_venda*q_vendida
    lucro_total = lucro_total + lucro_p

print(f"total de mercadorias: {total}")
print(f"Faturamento total: {faturamento_total}")
print(f"lucro total: {lucro_total}")