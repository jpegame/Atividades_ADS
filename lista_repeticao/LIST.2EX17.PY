'''
Ex.17 
'''
#Para dar início ao loping é preciso definir uns vaores iniciais para cada variável
precisao = 0.00001
pi = 0
v_fraçao = 1
denominador = 1
sinal = 1

# O looping vai acontecer enquanto o valor da fração for menor que q 0.00001
while abs(v_fraçao) >= precisao:
    pi = pi + (sinal * 4 /denominador)
    denominador = denominador + 2
    sinal = sinal * (- 1)
    v_fraçao = 4 / denominador
   
    

print("O valor de π com precisão de", precisao, "é:", pi)