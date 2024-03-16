'''
Elabore um outro programa didático nos mesmos moldes do anterior para treino da
divisão. Neste programa deve ser perguntado à criança o resultado da divisão e o
resto. '''
from random import randint

numero_perguntas = 0
numero_acertos = 0
numero_erros = 0
while True:
    n = int(input('Qual numero usado para dividir (1, 10)? '))
    numero_aleatorio = randint(1, 10 * n)
    
    resposta_errada = True
    while resposta_errada:
        print(f'Quanto é {numero_aleatorio} dividido por {n}?')
        resultado = int(input('Digite o resultado: '))
        resto = int(input('Digite o resto: '))

        if (resto == int(numero_aleatorio % n)) and resultado == int(numero_aleatorio // n):
            numero_acertos += 1
            resposta_errada = False
        else:
            print('Resposta errada!')
            numero_erros += 1
    numero_perguntas += 1
    if input('Deseja continuar? (S/N)') == 'N':
        break

print('Número de perguntas: ', numero_perguntas)
print('Número de acertos: ', numero_acertos)
print('Número de erros: ', numero_erros)
