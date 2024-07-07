'''Faça um programa para corrigir uma prova de múltipla escolha de 10 questões, cujo
gabarito é b, c, d, a, a, e, b, d, a, c. Cada questão vale 1,0 ponto e a nota será de 0,0 a
10,0. O programa deve ler do teclado o número de matrícula de até 30 alunos em um
vetor e suas respectivas respostas em uma matriz (que devem obrigatoriamente estar
entre "a" e "e". A seguir, o programa deve calcular e imprimir:
a. Para cada aluno, seu número e nota.
b. A porcentagem de alunos aprovados, sendo a menor nota para aprovação
igual a 6,0.'''

alunos = []
respostas = []
gabarito = ['b','c','d','a','a','e','b','d','a','c']

aprovados = 0 
while len(alunos) <= 30:
    user = input("Digite seu número de matricula: ")
    alunos.append(user)

    resposta = []
    contador = 1
    while contador <= 10:
        alternativa = input(f"Digite a alternativa da questão {contador}: ")
        if not alternativa in gabarito:
            print("\nApenas respostas entre A e E\n")
            continue

        resposta.append(alternativa)
        contador += 1 

    respostas.append(resposta)
    continua = input("Deseja continuar (s/n): ").lower()
    if continua == 'n':
        break

for i in range(len(alunos)):
    nota = 0 
    for j in range(len(gabarito)):
        if respostas[i][j] == gabarito[j]:
            nota += 1
    
    if nota >= 6: 
        aprovados += 1

    print(f"o aluno de matricula {alunos[i]} tirou {nota}")

porcentagem = (aprovados / (len(respostas))) * 100
print(f"A porcentagem de alunos aprovados é de {porcentagem:.2f}%")