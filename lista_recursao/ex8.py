'''Defina a função que recebe como argumento um número inteiro positivo e devolve
True se esse número for um número perfeito e False em caso contrário. Recorde que
um número perfeito é um número natural que é igual à soma de todos os seus
divisores próprios, isto é, a soma de todos os divisores excluindo o próprio número.
Pode, se assim o entender, definir funções auxiliares.'''

def soma_divisores(num, divisor):
    if divisor == num:
        return 0
    elif num % divisor == 0:
        return divisor + soma_divisores(num, divisor + 1)
    else:
        return soma_divisores(num, divisor + 1)

def numero_perfeito(num):
    if num <= 0:
        return False
    return num == soma_divisores(num, 1)

def main():
    x = int(input('Digite um número para verificar se ele é perfeito: '))
    if numero_perfeito(x):
        print('É número perfeito!')
    else:
        print('Não é número perfeito!')

main()