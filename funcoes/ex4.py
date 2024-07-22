'''Implemente um programa com uma função para calcular o número de combinações
possíveis de m elementos em grupos de n elementos (n ≤ m), dado pela fórmula de
combinação:
      𝑚!
  -----------
  (𝑚 - n)! n!'''

def fatorial(numero):
  fatorial = 1
  for num in range(1, numero + 1):
    fatorial *= num
  return fatorial

def formula(m, n):
  return fatorial(m) / (fatorial(m - n) * fatorial(n))

def main():
  while True:
    m = int(input('Digite o número de combinações (m): '))
    n = int(input('Digite o número de combinações (n): '))
    if n <= m:
      break

    print('\n n precisa ser maior ou igual a m \n')

  print(f'Resultado do cálculo: {formula(m,n):.2f}')

main()