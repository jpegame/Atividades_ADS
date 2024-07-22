"""Escreva uma função que imprime, linha a linha, os valores de uma matriz
bidimensional dada como argumento.
"""
def imprimir_matriz(matriz):

    for linha in matriz:
        for elemento in linha:
            print(elemento, end=' ')
        print()  # Move para a próxima linha após imprimir todos os elementos da linha

def receber_matriz():

    n = int(input("Digite o número de linhas da matriz: "))
    m = int(input("Digite o número de colunas da matriz: "))

    matriz = []
    for i in range(n):
        while True:
            linha = input(f"Digite os elementos da {i+1}ª linha separados por espaço: ").strip().split()
            if len(linha) == m:
                linha_int = []
                matriz_valida = True
                for elemento in linha:
                    if elemento.isdigit():
                        linha_int.append(int(elemento))
                    else:
                        matriz_valida = False
                        break
                
                if matriz_valida:
                    matriz.append(linha_int)
                    break
                else:
                    print("Entrada inválida. Todos os elementos devem ser números inteiros.")
            else:
                print(f"Número incorreto de elementos. A linha deve ter {m} elementos.")
    
    return matriz

def main():
    matriz = receber_matriz()
    print("A matriz é:")
    imprimir_matriz(matriz)

# Chama a função main para executar o programa
main()