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