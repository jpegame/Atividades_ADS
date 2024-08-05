"""Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve o número de elementos pares que existem nas
sublistas de w. Por exemplo, no caso da lista [[2,4,3,1],[3,5,7],[],[8,0,6]] a função deve
devolver 5.
"""

def contar_pares(w):
    if not w:  # Caso base: lista vazia
        return 0
    elif isinstance(w[0], list):  # Se o primeiro elemento é uma sublista
        return contar_pares(w[0]) + contar_pares(w[1:])
    else:  # Se o primeiro elemento é um número
        return (1 if w[0] % 2 == 0 else 0) + contar_pares(w[1:])

def obter_lista_usuario():
    lista_principal = []
    while True:
        entrada = input("Digite uma sublista de números inteiros separada por vírgulas (ou apenas pressione Enter para finalizar): ")
        print("=-"*30)
        if entrada.strip() == "":
            break
        sublista_str = entrada.split(',')
        try:
            sublista = [int(num) for num in sublista_str]
            lista_principal.append(sublista)
        except ValueError:
            print("Entrada INVÁLIDA! Certifique-se de digitar uma lista de números inteiros separados por vírgulas.")
            print("=-"*30)
    
    return lista_principal

def main():
    lista_usuario = obter_lista_usuario()
    print("Número de elementos pares:", contar_pares(lista_usuario))


main()

