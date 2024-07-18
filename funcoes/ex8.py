'''Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a
temperatura em graus C, sendo:
C = 5/9 * (F - 32). A seguir, faça um programa que, em
loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente,
utilizando a função FparaC.'''

def FparaC(F):
  return 5/9 * (F - 32) 

def main():
  while True:
    F = float(input('Digite a temperatura em graus Fahrenheit: '))
    print(f'A temperatura corresponde a {FparaC(F):.1f}°C')

    if input('Deseja continuar?(s/n) ').lower() == 'n':
      break

main()