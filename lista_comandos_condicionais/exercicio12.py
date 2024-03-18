'''
Uma empresa decidiu dar um bônus de Natal aos seus funcionários, cujo valor é
definido do seguinte modo:
a. Funcionários do sexo masculino com tempo de casa superior à 15 anos terão
direito à um bônus de 15% do seu salário.
b. Funcionárias com tempo de casa superior à 10 anos terão direito a um bônus
de 25% do seu salário.
c. Demais funcionários receberão um bônus de R$ 500,00
'''

tempo_casa = int(input('Digite o tempo de casa:'))
sexo_funcionario = input('Digite o sexo do funcionário: (M/F)')
salario = float(input('Digite o salário do funcionário: '))

if sexo_funcionario == 'M':
    if tempo_casa >= 15:
        bonus = 0.15 * salario
    else:
        bonus = 500
else:
    if tempo_casa >= 10:
        bonus = 0.25 * salario
    else:
        bonus = 500

print('O bônus é de: R$', bonus)