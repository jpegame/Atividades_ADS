"""Usando algoritmos recursivos, escreva funções que:
a. Calcule o produtório de um número m, n vezes.
b. Calcule a potência n de um número k.
c. Some os dígitos de um número inteiro não negativo.
d. Calcule a média dos dígitos de um número inteiro não negativo."""

def produtorio(m,n):
    if n == 0:
        return 1
    return m * produtorio(m,n - 1)

def potencia(k,n):
    if n == 0:
        return 1 #k^0 = 1
    return k * potencia(k, n-1)

def soma_digitos(num):
    if num == 0:
        return 0
    return num % 10 + soma_digitos(num//10)

def contar_digitos(num):
    if num == 0:
        return 0
    return 1 + contar_digitos(num//10)

def media_digitos(num):
    if num == 0:
        return 0
    soma = soma_digitos(num)
    count = contar_digitos(num)
    return soma/count

def menu():
    opcao = -1
    while opcao < 1 or opcao > 5:
        print("=" *45)
        print(
            '''
            [1] Produtório
            [2] Potência
            [3] Soma dos dígitos
            [4] Média dos dígitos
            [5] Sair
        '''
        )
        print("=" *45)

        try:

            opcao = int(input("Digite a sua opção: \n"))
            print("-="*30)

            if opcao < 1 or opcao > 5:
                print("Opção Inválida")
        except ValueError:
            print("Entrada INVÁLIDA! Por favor, escolha uma das opções acima.")
    return opcao

def verificar_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada INVÁLIDA! Por favor, insira um número inteiro")
        
def main():
    while True:
        escolha = menu()

        if escolha == 1:
            m = verificar_inteiro("Digite o valor de m: ")
            print("-"*30)
            n = verificar_inteiro("Digite o valor de n: ")
            resultado = produtorio(m,n)
            print("-="*30)
            print(f"Produtório de {m} e {n} é {resultado}")
        elif escolha == 2:
            k = verificar_inteiro("Digite a base k: ") 
            print("-"*30)
            n = verificar_inteiro("Digite o expoente n: ")
            resultado = potencia(k,n)
            print("-="*30)
            print(f"{k} elevado a {n} é {resultado}")
        elif escolha == 3:
            num = verificar_inteiro("Digite um número positivo inteiro: ")
            resultado = soma_digitos(num)
            print("-="*30)
            print(f"A soma dos dígitos do número {num} é {resultado}")
        elif escolha == 4:
            num = verificar_inteiro("Digite um número: ")
            resultado = media_digitos(num)
            print("-="*30)
            print(f"A médias dos dígitos de {num} é {resultado}")
        elif escolha == 5:
            print("-="*30)
            print("Saindo...")
            break
        else:
            print("Opção INVÁLIDA. Tente novamente...")

main()