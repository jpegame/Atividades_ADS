'''
Em uma loja de eletrodomésticos, os funcionários da seção de TVs recebem,
mensalmente um salário fixo mais comissão. Essa comissão é calculada em relação
ao tipo e número de televisores vendidos, de acordo com a tabela abaixo:
Tipo Quantidade vendida Comissões
8 K 10 ou mais R$ 550 por TV vendida
Menos que 10 R$ 350 por TV vendida
4 K 10 ou mais R$ 420 por TV vendida
Menos que 10 R$ 250 por TV vendida
7
Sabe-se ainda, que ele tem um desconto de 8% do salário total para pagamento do
INSS e se o seu salário total for superior a R$ 950,00 ele ainda tem um desconto de
5% do salário para fins de imposto de renda. Faça um programa que leia os dados de
vários funcionários e, para cada funcionário, calcule e imprima o salário líquido (já
com os descontos). Além disso, no final, o programa deve:
a. Imprimir o número de funcionários.
b. Imprimir o total de salários pagos.
c. Imprimir a média das comissões.
d. Imprimir o valor da maior e da menor comissão paga pelo departamento. '''

qtd_funcionarios = 0
salario_total = 0
comissao_lista = []
while True:
    salario = float(input('Qual o salário do funcionário? '))
    qtd_4k = int(input('Quantidade de TVs 4K vendidas: '))
    qtd_8k = int(input('Quantidade de TVs 8K vendidas: '))

    if qtd_4k >= 10:
        comissao_4k = 420 * qtd_4k
    else:
        comissao_4k = 250 * qtd_4k

    if qtd_8k >= 10:
        comissao_8k = 550 * qtd_8k
    else:
        comissao_8k = 350 * qtd_8k

    salario += (comissao_4k + comissao_8k)
    salario_liquido = 0.92 * salario # -8% do salário
    if salario_liquido > 950:
        salario_liquido *= 0.95 # -5% do salário
    print('Salário liquido: ',salario_liquido)

    qtd_funcionarios += 1
    salario_total += salario

    if comissao_4k:
        comissao_lista.append(comissao_4k)
    if comissao_8k:
        comissao_lista.append(comissao_8k)

    
    if input('Deseja inserir mais funcionarios? (S/N)') == 'N':
        break
print('----------------------------')
print('Número de funcionários: ', qtd_funcionarios)
print('Total de salário pago: ', salario_total)
print('Média das comissões: ', sum(comissao_lista) / len(comissao_lista))
print(f'Maior comissão: {max(comissao_lista)} || Menor comissão: {min(comissao_lista)}')