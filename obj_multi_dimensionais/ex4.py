# Escreva uma função que dada uma matriz (M), calcule a sua transposta (Mt).

def print_matriz(matriz, transposta=''):
  print(f'\nMatriz {transposta}')
  for linha in matriz:
    for item in linha:
      print(item, end=' ')
    print('')

def matriz_transposta(linhas, colunas, matriz):
  matriz_transposta = []
  for i in range(colunas):
    item = []
    for x in range(linhas):
      item.append(matriz[x][i])
    matriz_transposta.append(item)
  
  return matriz_transposta

def main():
  linhas = int(input("Quantidade de linhas da matriz: "))
  colunas = int(input("Quantidade de colunas da matriz: "))

  matriz = []
  for linha in range(linhas):
    item = []
    for coluna in range(colunas):
      print(f'\nO valor será inserido na linha {linha + 1}, coluna {coluna + 1}.')
      item.append(input("Insira um valor na matriz: "))

    matriz.append(item)

  Mt = matriz_transposta(linhas, colunas, matriz)

  print_matriz(matriz)
  print_matriz(Mt, transposta='Transposta')

main()