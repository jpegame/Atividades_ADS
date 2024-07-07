'''Escreva um programa que lê duas notas de vários alunos e armazena tais notas em
um dicionário, onde a chave é o nome do aluno. A entrada de dados deve terminar
quando for lida uma string vazia como nome. Seu programa deve também calcular a
média do aluno e exibir o nome e a média do aluno de maior média.'''

alunos_dict = {}

while True:
    nome = input("\nNome do aluno: ")
    if not nome:
        break
    
    notas = []
    for x in range(2):
        notas.append(float(input("Insira a nota: ")))
    alunos_dict[nome] = notas

nome_maior_media = ''
maior_media = 0
for v in alunos_dict:
    media_aluno = (alunos_dict[v][0] + alunos_dict[v][1])/2
    if (maior_media < media_aluno): 
        maior_media = media_aluno
        nome_maior_media = v

print(f'''
      Aluno com maior média: {nome_maior_media}
      Valor da maior média: {maior_media}
      ''')