print("=-"*30)
print("SOMADOR DE MATRIZES")
print("=-"*30)
print()
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))


matriz1 = []
matriz2 = []
soma_matriz = []

print("Digite os valores da primeira matriz: ")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valores = int(input(f"Digite o valor para posição {[i + 1],[j +1 ]}: "))
        linha.append(valores)
    matriz1.append(linha)
print("Digite os valores da segunda matriz: ")
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valores = int(input(f"Digite os valor para posição {[i+1],[j+1] }: "))
        linha.append(valores)
    matriz2.append(linha)

for i in range(linhas):
    linha_soma = []
    for j in range(colunas):
        linha_soma.append(matriz1[i][j] + matriz2[i][j])
    soma_matriz.append(linha_soma)
print(f"\nSoma das matrizes:")
for linha in soma_matriz:
    print(linha)