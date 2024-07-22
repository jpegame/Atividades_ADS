"""Escreva um programa com uma função que, dado um número inteiro (n > 1), retorne
uma lista com os fatores primos de n."""



def fatores_primos(n):
    fatores = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            fatores.append(divisor)
            n //= divisor
        divisor += 1
    return fatores

def main():
    while True:
        entrada = input("Digite um número maior que 1: ")
        if entrada.isdigit() and int(entrada) > 1:
            n = int(entrada)
            break
        else:
            print("-="*30)
            print("Entrada INVÁLIDA! Por favor, digite um NÚMERO que seja MAIOR que 1!")
            print("-="*30)

    fatores = fatores_primos(n)
    print("-="*30)
    print(f"Os fatores primos de {n} são: {fatores}")

main()