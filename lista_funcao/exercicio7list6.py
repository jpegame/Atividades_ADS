"""Crie um programa que implemente e teste uma função que, dadas duas listas
representando dois conjuntos:
a. Retorne uma lista que represente a união dos dois conjuntos.
b. Retorne uma lista que represente a interseção dos dois conjuntos.
c. Retorne uma lista que represente a diferença entre os dois conjuntos.
d. Verifique se o primeiro é um subconjunto do segundo."""

def uniao(conjunto1,conjunto2):
    uniao_resultado = conjunto1[:]
    for elemento in conjunto2:
        if elemento not in uniao_resultado:
            uniao_resultado.append(elemento)
    return uniao_resultado

def intersecao(conjunto1,conjunto2):
    intersecao_resutado = []
    for elemento in conjunto1:
        if elemento in conjunto2 and elemento not in intersecao_resutado:
            intersecao_resutado.append(elemento)
    return(intersecao_resutado)

def diferenca(conjunto1,conjunto2):
    diferenca_resultado = []
    for elemento in conjunto1:
        if elemento not in conjunto2:
            diferenca_resultado.append(elemento)
    for elemento in conjunto2:
        if elemento not in conjunto1:
            diferenca_resultado.append(elemento)
    return diferenca_resultado

def subconjunto(conjunto1,conjunto2):
    for elemento in conjunto1:
        if elemento not in conjunto2:
            return False
    return True

def receber_conjuntos():
    tipo = input("Escolha o tipo dos conjuntos (Letras | Numeros | Ambos): ").strip().lower()
    while tipo not in ["letras", "numeros","ambos"]:
        tipo = input("Escolha INVÁLIDA! Escolha o tipo dos conjuntos (Letras | Numeros | Ambos): ").strip().lower()

    tamanho = int(input("Digite o tamanho dos conjuntos: "))

    conjunto1 = []
    conjunto2 = []

    def validar_entrada(valor):
        if tipo == "letras" and valor.isalpha():
            return True
        elif tipo == "numeros" and valor.replace('.', '', 1).isdigit():
            return True
        elif tipo == "ambos":
            if valor.isalpha() or valor.replace('.', '', 1).isdigit():
                return True
        return False

    print("Digite os valores do conjunto 1: ")
    for i in range(tamanho):
        valor = input(f"Digite o {i+1}° valor do conjunto1: ").strip()
        while not validar_entrada(valor):
            valor = input(f"Valor INVÁLIDO!! Digite o {i+1}° valor do conjunto1: ").strip()
        conjunto1.append(valor)

    print("Digite os valores do conjunto2: ")
    for i in range(tamanho):
        valor = input(f"Digite o {i+1}° valor do conjunto2: ").strip()
        while not validar_entrada(valor):
            valor = input(f"Valor INVÁLIDO!! Digite o {i+1}° valor do conjunto2: ").strip()
        conjunto2.append(valor)

    return conjunto1, conjunto2
def main():
    conjunto1,conjunto2 = receber_conjuntos()

    print(f"O conjunto1 é: {conjunto1}")
    print(f"O conjunto2 é: {conjunto2}")

    print("União dos conjuntos:",uniao(conjunto1,conjunto2))
    print("Interseção dos conjuntos:",intersecao(conjunto1,conjunto2))
    print("Diferença entre os dois conjuntos:",diferenca(conjunto1,conjunto2))
    print("Conjunto1 é subconjunto de conjunto2?:",subconjunto(conjunto1,conjunto2))

main() 






#receber como string a entrada