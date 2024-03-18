
"""
15. Calculo a soma dos 10 primeiros termos da série:
100/0! + 99/1! + 98/2! + 97/3! + ....

"""
soma = 0
fatorial = 1
for i in range(0, 9):
    soma += (100 - i) / fatorial
    fatorial = fatorial * (i + 1) #Essa é a fórmula para calcular o valor do fatorial de acordo com o termo pedido
  


print(f"Soma dos 10 primeiros termos da série: {soma}")