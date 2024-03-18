"""
13. Elabore um programa que receba três valores quaisquer e imprima o menor valor dos
três lidos. O que acontece se o seu programa tiver lido dois ou mais números iguais
(Ex.: 1, 1, 3)?
"""
#Pedi para que a pessoa inserir 3 valores
Valor1 = float(input("Informe o primeiro valor: "))
Valor2 = float(input("Informe o segundo valor: "))
Valor3 = float(input("Informe o terceiro valor: "))

#Defini a variável de menor valor com um valor qualquer
Menor_Valor = Valor1

#E adicionei as condições comparando uma com a outra até chegar no número de menor valor
if Valor2 < Menor_Valor:
    Menor_Valor = Valor2

if Valor3 < Menor_Valor:
    Menor_Valor = Valor3

print(f"O menor valor é: {Menor_Valor:.2f}")

'''
Se por acaso a pessoa adicionar números iguais (ex: 1, 1, 5) o programa definirá normalmente 
a variável de menor valor (nesse caso o número 1)
'''