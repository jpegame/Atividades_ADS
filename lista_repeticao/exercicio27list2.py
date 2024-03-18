"""
O custo de produção de um livro é constituído dos custos por página, mais o custo
de encadernação, além do custo fixo. O custo por página impressa é de R$0,03, o
custo fixo é de R$ 4397,00 e o custo de encadernação depende de cada livro, sendo
utilizada a seguinte tabela:
• Encadernação simples: R$4,30
• Encadernação especial: R$7,80
• Encadernação luxo: R$10,50
Faça um programa que leia para uma lista de livros: o número de páginas, o tipo de
encadernação e o número de vendas previstas (número de cópias) e:
a. Calcule o preço mínimo de cada livro para que cubra os custos de produção e
o preço de venda para que a editora tenha um lucro de 20%.
b. Imprima o total de livros analisados.
c. Imprima o preço médio de venda dos livros (com lucro de 20%).
d. Imprima o preço de venda dos livros mais barato e mais caro. 
"""

custo_fixo = 4397.0
pagina = 0.03
custos_encadernacao = {
    1: 4.30,
    2: 7.80,
    3: 10.50
}

total_livros = 0 
preco_venda_total = 0 
preco_venda_minimo = 9999999
preco_venda_maximo = 0
print("Para parar os lançamentos, digite 0")
while True:
    num_pag = int(input("Digite o número de paginas do livro: "))
    if num_pag == 0:
        break
    encadernacao = int(input("Qual o tipo de encadernação? (1 - Simples, 2- Especial, 3- Luxo): "))
    copias_vendidas = int(input("Digite o número de cópias que serão vendidas: "))

    custo_encadernacao = custos_encadernacao.get(encadernacao, 0)
    preco_minimo = custo_fixo + (pagina*num_pag) + custo_encadernacao
    preco_venda = preco_minimo * 1.20

    total_livros = total_livros + 1
    preco_venda_total += 1

    if preco_venda < preco_venda_minimo:
        preco_venda_minimo = preco_venda
    if preco_venda > preco_venda_maximo:
        preco_venda = preco_venda_maximo

if total_livros > 0:
    preco_medio = preco_venda_total/total_livros
else:
    preco_medio = 0

print(f"Total de livros análisados: {total_livros}")
print(f"Preço médio de venda dos livros: R${preco_medio}")
print(f"Preço de venda do livro mais barato: R${preco_venda_minimo}")
print(f"Preço de venda do livro mais caro: R${preco_venda_maximo}")


