def é_matriz_diagonal(matriz):

    n = len(matriz)
    
    for i in range(n):
        for j in range(n):
            if i != j and matriz[i][j] != 0:
                return False
    return True

def receber_matriz():

    n = int(input("Digite a ordem da matriz quadrada: "))

    matriz = []
    for i in range(n):
        while True:
            linha = input(f"Digite os elementos da {i+1}ª linha separados por espaço: ").strip().split()
            # Verificar se o número de elementos é correto
            if len(linha) == n:
                # Verificar se todos os elementos são números inteiros
                matriz_valida = True
                linha_int = []
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
                print(f"Número incorreto de elementos. A linha deve ter {n} elementos.")
    
    return matriz

def main():
    matriz = receber_matriz()
    
    if é_matriz_diagonal(matriz):
        print("A matriz é uma matriz diagonal.")
    else:
        print("A matriz não é uma matriz diagonal.")

main()

