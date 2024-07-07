inputs = []
while True:
  input_var = input('Escreva uma linha:')
  if not input_var:
    break

  inputs.append(input_var)

while True:
  input_var = input('Digite um comando:')
  if input_var.lower() == 'i':
    for input_str in inputs:
      print(input_str)
  elif input_var.lower() == 't':
    linha_num = 1
    linhas = []
    while  True:
      linha_digitada = int(input(f'Digite o número da {linha_num}° linha a ser trocada: '))
      if len(inputs) >= linha_digitada and linha_digitada:
        linhas.append(linha_digitada)
        linha_num += 1
      else:
        print('Número da inválida')
      
      if len(linhas) == 2:
        l1 = linhas[0] - 1
        l2 = linhas[1] - 1
        inputs[l1], inputs[l2] = inputs[l2], inputs[l1]
        break
  elif input_var.lower() == 'r':
    while  True:
      linha_digitada = int(input('Digite o número da linha a ser redigitada: '))
      if len(inputs) >= linha_digitada and linha_digitada:
        inputs[linha_digitada - 1] = input('Escreva a linha: ')
        break
      print('Número da inválida')
  elif input_var.lower() == 's':
    break
  else:
    print('Comando inexistente!')
