'''Faça um programa que leia as dimensões de uma matriz qualquer (no máximo 30x30),
leia seus elementos e imprima a sua transposta.'''

linhas = int(input("Quantidade de linhas: "))
colunas = int(input("Quantidade de colunas: "))
matriz = []

for x in range(linhas):
    temp = []
    for n in range(colunas):
        temp.append(input("Insira um valor na matriz: "))
    matriz.append(temp)

matriz_transposta = []
for i in range(colunas):
    temp = []
    for x in range(len(matriz)):
        temp.append(matriz[x][i])
    matriz_transposta.append(temp)

print(f"Matriz: {matriz}") 
print(f"Matriz transposta: {matriz_transposta}")