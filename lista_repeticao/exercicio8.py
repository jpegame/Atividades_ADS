'''Numa universidade, o sistema de avaliação é o seguinte: para passar direto, o aluno
precisa ter média do período (mp) igual ou superior a 7 pontos. Caso contrário, o
aluno será submetido a exame final, sendo a sua média final (mf) calculada pela
seguinte fórmula: mf = 0.6mp + 0.4ne, onde ne é a nota do exame. Essa média final
deverá então ser igual ou superior a 5 pontos para que o aluno seja aprovado. Por
outro lado, a média do período é calculada através da média das notas dos créditos,
cujo número é diferente para cada disciplina. Faça um programa que leia do usuário o
número de créditos da disciplina, as notas dos créditos, e se necessário calcule a
nota que o aluno precisa tirar no exame final para ser aprovado. Se antes de terminar
todos os créditos o aluno já estiver aprovado, avise isso a ele e encerre a leitura de
notas (utilize aqui um comando break). '''

n_creditos = int(input('Digite o número de créditos:'))
notas = 0
for i in range(n_creditos):
    notas += float(input('Digite a nota:'))
    media = notas / n_creditos
    if media >= 7:
        response = 'O aluno já possui nota o suficiente para ser aprovado.'
        break
    
if media < 7:
    exame = (5 - 0.6 * media) / 0.4
    response = f'O aluno precisa tirar no mínimo {exame:.3f} no exame para aprovar.'

print(response)