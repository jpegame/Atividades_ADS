'''
Para enviar mensagens que não devem ser lidas por estranhos, pode-se codificá-las.
Faça um programa que leia uma frase e a seguir codifique essa frase da seguinte
forma: cada letra que se encontra em posição ímpar na tabela ASCII tem este seu
valor ASCII dividido por 2, e cada letra que se encontra em posição par na mesma
tabela é trocada por outra, 3 posições atrás dela da tabela. No final, imprima a frase
codificada.'''
# chr ascii to string
# ord string to ascii

list_str = list(input('Digite a frase a ser decodificada: '))
for index, item in enumerate(list_str):
  if ord(item) % 2:
    list_str[index] = chr(ord(item) // 2)
  elif item != ' ':
    list_str[index] = chr(ord(item) - 3)

print(''.join(list_str))