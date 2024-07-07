'''Faça um programa que leia nomes de alunos e suas respectivas notas até que o
nome "oooo" seja informado, após o fim da leitura, exiba o nome do aluno que possui
a maior nota. Obs.: Use dicionário para resolver essa questão.'''

notas_dict = {}
while True:
    nome = input('Digite o nome do aluno: ')
    if nome == 'oooo':
        break
    
    nota = float(input('Digite a nota do aluno: '))
    notas_dict[nome] = nota

nota_max = {
    'nome': '',
    'nota': 0
}
for key in notas_dict.keys():
    if notas_dict[key] > nota_max['nota']:
        nota_max['nome'] = key
        nota_max['nota'] = notas_dict[key]

print(f'O aluno com a maior nota é: {nota_max["nome"]} | NOTA: {nota_max["nota"]}')