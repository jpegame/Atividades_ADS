'''
Elabore um programa que calcule e mostre o fatorial de um número (N!), sendo que N
é fornecido pelo usuário.
Sabemos que:
N! = 1 x 2 x 3 x 4 x. . .x (N - 1) x N;
0! = 1, por definição.'''

n = int(input('Digite um número para o calculo do fatorial:'))

fatorial = 1
for numero in range(1, n + 1, 1):
    fatorial *= numero

print(f'{n}! = {fatorial}')