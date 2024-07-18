'''Escreva uma função que dada uma matriz quadrada, 
verifique se ela é uma matriz triangular inferior.'''

def print_matriz(matriz):
  print(f'\nMatriz:')
  for linha in matriz:
    for item in linha:
      print(item, end=' ')
    print('')

def is_triangular_inferior(matriz):
  n = len(matriz)
  for i in range(n): #Percorre as linhas
    for j in range(i + 1, n): #Percorre as colunas
      if matriz[i][j] != 0:
        return False
      
  return True

def main():
  tamanho = int(input("Digite o tamanho da matriz: "))
  matriz = []
  for num_linha in range(tamanho):
    item = []
    for coluna in range(tamanho):
      print(f'\nO valor será inserido na linha {num_linha + 1}, coluna {coluna + 1}.')
      item.append(int(input("Insira um valor na matriz: ")))

    matriz.append(item)

  print_matriz(matriz)
  if is_triangular_inferior(matriz):
    print('É triângular inferior!')
    return
  
  print('Não é triângular inferior!')

main()