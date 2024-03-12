from datetime import datetime

now = datetime.now() #Recupera a data do momento de execução do codigo
maioridade = 18
day, month, year = [int(x) for x in input("Digite o seu aniversário (DD/MM/YYYY): ").split('/')] #Separa a data de nascimento do usuário em três diferentes variáveis
'''
O .split('/') separa a string em items de uma lista baseado no caracter dentro do parentêses, no caso a barra, por exemplo:
input: '01/01/2001' o split separa em items de uma lista: ['01','01','2001'] e o for percorre os items da lista os salvando
na variavel x que é transformada de string para um inteiro e cada item é definido para uma das variaveís na ordem do input
'''

year_diff = now.year - year
if year_diff > maioridade:
    print('Maior de idade')    
elif year_diff < maioridade:
    print('Menor de idade')
else:
    if month < now.month:
        print('Maior de idade')
    elif month > now.month:
        print('Menor de idade') 
    else:
        if day < now.day:
            print('Maior de idade')
        else:
            print('Menor de idade')