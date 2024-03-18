'''
9. Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a
exercícios sobre o mesmo assunto até que ele alcance a nota máxima (100 pontos),
para só então passar ao assunto seguinte. Entretanto, se após 5 tentativas no mesmo
nível o aluno obtiver menos de 300 pontos acumulados ele retorna ao nível anterior.
Caso contrário, ele permanece no mesmo nível, zerando novamente os pontos
acumulados. Faça um programa que compute o progresso do aluno, através da 
leitura de suas notas até que ele termine o 10º nível. Utilize o comando break (por
exemplo, para passar ao próximo nível e recomeçar quando o aluno tiver tirado a nota
máxima).
'''

nivel = 1
pontos_acumulados = 0
tentativas = 0

while nivel <= 10: 

    nota = int(input(f"Você está no nivel {nivel}, insira sua nota: ")) 
    tentativas = tentativas + 1
    pontos_acumulados = pontos_acumulados + nota

    if nota == 100 and nivel < 10:
        print("Parabéns, vc avançou um nível") 
        nivel = nivel + 1
        tentativas = 0
        pontos_acumulados = 0
        
    elif nota == 100 and nivel == 10:
        print("Parabéns vc chegou no último nível")
        break

    elif tentativas == 5: 
        if pontos_acumulados < 300:
            nivel = nivel - 1
            print("Você não alcançou 300 pontos, volte 1 nível")
        else:
            tentativas = 0
            pontos_acumulados = 0

    

    
        