'''
Para fazer uma pesquisa sobre o consumo de energia elétrica de uma cidade, são
fornecidos os seguintes dados:
• O preço o kWh
• O número de identificação de cada consumidor
• A quantidade de kWh consumido no mês por cada um
• O código do tipo de consumidor (residencial, comercial ou industrial)
A partir desses dados calcule:
a. Para cada consumidor, o total à pagar;
b. O maior consumo verificado;
c. O menor consumo verificado
d. O total de consumo (em kWh) para cada um dos três tipos de consumidores
e. A média de consumo (em kWh) para cada um dos três tipos de consumidores
f. O total arrecadado pela companhia elétrica. '''

kwh = float(input('Informe o preço do kWh:'))
consumidor_lista = []

while True:
    consumidor = input('Informe o número de identificação do consumidor:')
    consumo = float(input('Informe a quantidade de kWh consumido no mês por cada consumidor:'))
    tipo_consumidor = input('Informe o tipo de consumidor (residencial, comercial ou industrial):')
    menor_consumo = consumo
    consumidor_lista.append([consumidor, consumo, tipo_consumidor])

    if input('Deseja inserir mais consumidores? (S/N)') == 'N':
        break

residencial_soma = 0
qtd_residencial = 0

comercial_soma = 0
qtd_comercial = 0

industrial_soma = 0
qtd_industrial = 0

maior_consumo = 0
print('---------------------------')
for consumidor in consumidor_lista:
    numero = consumidor[0]
    consumo = consumidor[1]
    tipo_consumidor = consumidor[2]

    print(f'Consumidor do número {numero} tem que pagar R${consumo * kwh}')
    if consumo > maior_consumo:
        maior_consumo = consumo
    if consumo < menor_consumo:
        menor_consumo = consumo

    if tipo_consumidor == 'residencial':
        residencial_soma += consumo
        qtd_residencial += 1
    elif tipo_consumidor == 'comercial':
        comercial_soma += consumo
        qtd_comercial += 1
    elif tipo_consumidor == 'industrial':
        industrial_soma += consumo
        qtd_industrial += 1

print('---------------------------')
print('O maior consumo verificado: ', maior_consumo)
print('O menor consumo verificado: ', menor_consumo)
print('Total de consumo do residencial: ', residencial_soma)
print('Total de consumo do comercial: ', comercial_soma)
print('Total de consumo do industrial: ', industrial_soma)
print('Média de consumo do residencial: ', residencial_soma / qtd_residencial)
print('Média de consumo do comercial: ', comercial_soma / qtd_comercial)
print('Média de consumo do industrial: ', industrial_soma / qtd_residencial)
print('Total arrecadado: ', (residencial_soma + comercial_soma + industrial_soma) * kwh)
print('---------------------------')