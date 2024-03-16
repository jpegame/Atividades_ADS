n = int(input('Digite um número:'))

soma = 0
for numero in range(1, n + 1, 1):
    if numero % 2 == 0:
        soma -= 1 / numero
    else:
        soma += 1 / numero

print('O valor da série: ', soma)