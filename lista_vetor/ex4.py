'''
Um armazém trabalha com um determinado número de mercadorias diferentes (um
máximo de 100 itens). Faça um programa que leia e armazene em vetores os preços
de cada mercadoria e a quantidade vendida no mês e, além disso, calcule e imprima:
a. O faturamento mensal do armazém.
b. A mercadoria mais vendida e a menos vendida.
c. O preço da mercadoria menos vendida.
2
d. Quantas mercadorias têm seu preço mais alto que o preço da mercadoria
menos vendida.'''

max_mercadorias = 100
precos = [0] * max_mercadorias
quantidades = [0] * max_mercadorias

while True:
  num_mercadorias = int(input("Digite o número de mercadorias: "))
  if num_mercadorias < max_mercadorias and num_mercadorias > 0:
    break
  print('Número de mercadorias inválido')
  

faturamento = 0
for i in range(num_mercadorias):
  precos[i] = float(input(f"Digite o preço da {i + 1}° mercadoria: "))
  quantidades[i] = int(input(f"Digite a quantidade vendida da {i + 1}° mercadoria: "))
  faturamento += precos[i] * quantidades[i]


index_mais_vendida, index_menos_vendida = 0, 0
for i in range(1, num_mercadorias):
    if quantidades[i] > quantidades[index_mais_vendida]:
        index_mais_vendida = i
    if quantidades[i] < quantidades[index_menos_vendida]:
        index_menos_vendida = i


num_maior_que_menos_vendida = 0
for i in range(num_mercadorias):
    if precos[i] > precos[index_menos_vendida]:
        num_maior_que_menos_vendida += 1

print(f"\nFaturamento mensal: R${faturamento:.2f}")
print(f"Mercadoria mais vendida: Mercadoria {index_mais_vendida + 1}")
print(f"Mercadoria menos vendida: Mercadoria {index_menos_vendida + 1}")
print(f"Preço da mercadoria menos vendida: R${precos[index_menos_vendida]:.2f}")
print(f"Número de mercadorias com preço maior que a menos vendida: {num_maior_que_menos_vendida}")