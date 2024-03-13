n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

'''
Resto quando o divisor é maior que dividendo, o resto sempre retorna o dividendo.

Dado um input: 24 - 15
n1, n2 = 15, 9
n1, n2 = 9, 6
n1, n2 = 6, 3
n1, n2 = 3, 0

Dado um input: 30 - 12
n1, n2 = 12, 6
n1, n2 = 6, 0

Dado um input: 12 - 30
n1, n2 = 30, 12
n1, n2 = 12, 6
n1, n2 = 6. 0
'''

while n2 != 0:
    n1, n2 = n2, n1 % n2

print(n1)