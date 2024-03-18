"""
8. Faça um programa que leia o ano de nascimento de uma pessoa e imprima se ela é
maior ou menor de idade. Declare o ano atual e o limite de maioridade como
constantes simbólicas.

9. O que acontece no programa anterior se a pessoa nasceu há 18 anos, mas ainda não
fez aniversário? Melhore o programa para que, neste caso, o programa pergunte se a
pessoa já fez aniversário ou não antes de imprimir o resultado. 
"""
#Constantes Simbólicas
Ano_Atual = 2024
Limite_Maioridade = 18

#Declarei variáveis para a pessoa informar o ano em que ela nasceu e calcular a idade
Ano_Nascimento = int(input("Informe em que ano você nasceu: "))
Idade = Ano_Atual - Ano_Nascimento

#Condição para ser maior de idade: 1-Se fizer 18 no Ano_Atual; 2- Mais de 18 anos 3-Menos de 18 anos
if Idade == Limite_Maioridade: 
    Fez_Aniversario = input("Você já fez aniversário esse ano? Responda com (S/N): ").upper() #Converte para maiúscula
    if Fez_Aniversario == 'S':
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")
elif Idade > Limite_Maioridade:
    print("Você é maior de idade")
else:
    print("Você é menor de idade") 