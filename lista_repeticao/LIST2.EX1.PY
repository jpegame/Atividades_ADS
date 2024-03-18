'''
1. A população americana, em um determinado ano, ultrapassa a população brasileira.
No entanto, a taxa de crescimento aqui é de 4% ao ano e lá é de 2% ao ano. Faça um
programa para calcular em que ano a população brasileira irá ultrapassar a
americana.
'''

#Primeiro eu defini a população dos dois países e o valor do ano em que se inicia a contagem
p_brasileira = 200000000
p_eua = 340000000
ano = 2024

'''
Enquanto a população brasileira for menor ou igual a populaçao dos eua, somar a porcentagem da 
taxa de crescimento a cada ano, até que a população brasileira ultrapasse a população americana
e assim o "while" acaba
'''

while p_brasileira <= p_eua:
    p_brasileira = p_brasileira*1.04
    p_eua = p_eua*1.02
    ano = ano + 1

print(f"O ano em que o Brasil ultrapassará os EUA em população é {ano}")

