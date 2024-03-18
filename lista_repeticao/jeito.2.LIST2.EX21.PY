'''
Faça um programa didático para estudo das raízes quadradas dos números, da
seguinte forma: o programa gera um número aleatório, eleva ao quadrado e pergunta
qual a raiz quadrada desse valor para o estudante. O programa deve apresentar as
mensagens de erro e incentivo e os números de perguntas, acertos e erros de forma
semelhante aos anteriores. 
'''
import random
import math

acertos = 0
erros = 0
total_perguntas = 0

#Enquanto um número aeatorio for gerado, eleva-lo a 2 e perguntar a raiz desse valor
while True:

    n_aleatorio = random.randint(1, 20)
    n_ao_quadrado = n_aleatorio**2
    resposta = int(input(f"Qual a raiz quadrada de {n_ao_quadrado}?: "))
    
    if resposta == math.sqrt(n_ao_quadrado):
        print("Parabéns você acertou a resposta!")
        acertos += 1
        
    else:
        print(f"Você errou a resposta! A raiz quadrada de {n_ao_quadrado} é {n_aleatorio}")
        erros +=1

    total_perguntas += 1

    continuar = input("Deseja continuar estudando? (S/N): ").upper()
    if continuar == "N":
        break

print("-------------------------------------------")
print(f"Você respondeu {total_perguntas} perguntas")
print(f"Total de acertos: {acertos}")
print(f"Total de erros: {erros}")