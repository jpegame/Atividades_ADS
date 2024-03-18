'''
13. A série de Fibbonacci é gerada da seguinte forma: os dois primeiros termos são 1, os
demais são dados pela soma dos dois anteriores. Faça um programa que imprima os
“n” primeiros termos da série, sendo “n” dado pelo usuário. 
'''


s_fibbonacci = [1, 1] #Defini os dois primeiros termos da lista 

n = int(input("Digite o número de termos desejado: ")) #Solicitei o n de termos da sequência

# Criei um looping para definir o próximo termo da lista de acordo com a quantidade de termos pedida
for i in range (2, n):
    proximo_termo = s_fibbonacci[-1] + s_fibbonacci[-2]
    s_fibbonacci.append(proximo_termo)
    
# Criei mais um looping para mostrar ao usuário cada termo pedido
print(f"Os {n} primeiros termos da série de fibbonacci são: ")
for termo in s_fibbonacci:
    print(termo, end=" ")