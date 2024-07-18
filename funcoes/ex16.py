'''Faça um programa que calcule o imposto de renda de um contribuinte de um país imaginário
onde as regras do imposto são as seguintes:
• Todos pagam a mesma alíquota, de 20%.
• São descontados da base de cálculo (proventos) as despesas com educação e despesas médicas.
• São descontados R$ 1000,00 por dependente.
• O imposto devido ou a receber pode ser parcelado em até 6 vezes.
• Valores de imposto (devido ou a receber) abaixo de R$100,00 não são cobrados nem pagos.'''

def calcular_imposto(salario, despesa_educacao, despesa_medica, qtd_dependentes):
  aliquota = 0.2 # 20%
  desconto_dependente = 1000

  imposto_desconto = salario - despesa_educacao - despesa_medica - (qtd_dependentes * desconto_dependente)
  return imposto_desconto * aliquota

def main():
  salario = float(input('Digite o valor do salário: '))
  despesa_educacao = float(input('Digite o valor das despesas com educação: '))
  despesa_medica = float(input('Digite o valor das despesas médicas: '))
  qtd_dependentes = int(input('Digite o número de dependentes: '))

  while True:
    num_parcelas = int(input('Digite o número de parcelas: '))
    if num_parcelas > 0 and num_parcelas < 6:
      break
    print('Número de parcelas inválidas')

  imposto = calcular_imposto(salario, despesa_educacao, despesa_medica, qtd_dependentes)
  if imposto < 100:
    print('Não precisa ser pago imposto.')
  else:
    print(f'O imposto pode ser pago ou recebido com {num_parcelas} parcela(s) de R${(imposto / num_parcelas):.2f}')

main()