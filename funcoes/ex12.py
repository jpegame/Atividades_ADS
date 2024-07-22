'''Escreva uma função que calcule o valor de π, com precisão dada como parâmetro. '''

def calculo_pi(precisao):
  pi = 0
  divisor = 1
  for num in range(1, precisao + 1):
    if num % 2 == 0:
      pi -= 4 / divisor
    else:
      pi += 4 / divisor

    divisor += 2
  return pi

def main():
  precisao_pi = int(input('Digite a precisão desejada para o cálculo de π: '))
  valor_pi = calculo_pi(precisao_pi)

  print(f'O valor de π com precisão de {precisao_pi} termos é {valor_pi}')

main()