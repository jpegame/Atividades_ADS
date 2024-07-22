def é_matriz_permutacoes(matriz):

    n = len(matriz)
    
    # Verificar cada linha
    for i in range(n):
        um_contador = 0
        for j in range(n):
            if matriz[i][j] == 1:
                um_contador += 1
            elif matriz[i][j] != 0:
                return False
        if um_contador != 1:
            return False

    # Verificar cada coluna
    for j in range(n):
        um_contador = 0
        for i in range(n):
            if matriz[i][j] == 1:
                um_contador += 1
            elif matriz[i][j] != 0:
                return False
        if um_contador != 1:
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
                linha_int = []
                matriz_valida = True
                for elemento in linha:
                    if elemento == '0' or elemento == '1':
                        linha_int.append(int(elemento))
                    else:
                        matriz_valida = False
                        break
                
                if matriz_valida:
                    matriz.append(linha_int)
                    break
                else:
                    print("Entrada inválida. Todos os elementos devem ser 0 ou 1.")
            else:
                print(f"Número incorreto de elementos. A linha deve ter {n} elementos.")
    
    return matriz

def main():
    matriz = receber_matriz()
    
    if é_matriz_permutacoes(matriz):
        print("A matriz é uma matriz de permutações.")
    else:
        print("A matriz não é uma matriz de permutações.")

main()
