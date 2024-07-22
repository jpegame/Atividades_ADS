alunos_notas = {}
while True:
    nome = input("Digite o nome do aluno: ")
    if nome == "oooo":
        break
    notas = float(input("Digite a nota do aluno: "))
    print("-"*40)
    if notas < 0 or notas > 10:
        print("Nota inválida!! Tente novamente")
        break
    alunos_notas[nome] = notas

maior_nota = -1
aluno_Mnota = ""
print("=-"*30)
for aluno,notas in alunos_notas.items():
    if notas > maior_nota:
        maior_nota = notas
        nome_alMnota = aluno
print(f"O Aluno com a maior nota foi o(a) {nome_alMnota} , nota {maior_nota}")