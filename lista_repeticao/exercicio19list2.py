'''
Faça um programa didático para estudo de tabuadas de 1 até 10, onde:
a. A criança escolhe a tabuada a ser estudada.
b. O programa gera um número aleatório e pergunta à criança qual o valor dele
multiplicado pela tabuada escolhida. Se a criança errar, o programa pergunta
novamente, se acertar o programa pergunta à criança se ela deseja continuar
respondendo.
c. Ao final, o programa deve imprimir o número de perguntas respondidas, o
número de acertos e o número de erros cometidos pela criança.
'''
import random

print("       +---------------------------------------+")
print("       |    BEM-VINDO AO NOSSO JOGO DIDÁTICO   |")
print("       |                 DE                    |")
print("       |             MATEMÁTICA                |")
print("       +---------------------------------------+")
print(end="\n\n")

print("+----------------------------------------------------+")
print("|                     Regras                         |")
print("+----------------------------------------------------+")
print("| 1- Você deve escolher qual tabuada quer estudar    |")
print("+----------------------------------------------------+")
print("|2- Se acertar a pergunta feita pelo programa,       |")
print("|você decide se irá seguir para a proxima pergunta   |")
print("|ou não                                              |")
print("|----------------------------------------------------|")
print("|3- Caso erre, você terá mais chances de acertar     |")
print("|----------------------------------------------------|")
print("|4- A cada erro corrigido, automaticamente apare-    |")
print("|cera uma outra pergunta em seguida, como forma de   |")
print("|desafio, para que você possa ter um foco maior      |")
print("|----------------------------------------------------|")
print("|5- Caso queira parar de jogar, apenas escolher a    |")
print("|opção 'não' na pergunta 'deseja continuar?          |")
print("|----------------------------------------------------|")
print("|6- Ao fim do jogo aparecerá o número de perguntas   |")
print("|respondidas, o número de erros e o numero de acertos|")
print("+----------------------------------------------------+",end="\n\n")

escolha = int(input("Escolha uma tabuada para estudar:"))
palpite = 0
acerto = 0
erro = 0                  
while True:
    num_pc = random.randint(0,10)
    resposta = int(input(f"Qual o resultado da muliplicação {escolha} X {num_pc}?: "))
    palpite += 1
    result = num_pc * escolha
    
    if resposta == result:
        print("Você acertou!!! Parabêns")   
        print("Deseja continuar respondendo desafios?? (Responda com 1 ou 2)")
       
        acerto += 1
        decisao_acerto = int(input(" 1 - Sim   |   2 - Não : "))
        

        if decisao_acerto == 2: 
            break
    else:
        while resposta != result:
            erro += 1
            
            print("Você errou, tente novamente, vamos lá você consegue")
            resposta = int(input(f"Quanto é {escolha} X {num_pc}?: "))
            
            print(end="\n\n")

print(f"O numero de perguntas respondidas foi {palpite}")
print(f"O numero de acertos foi {acerto}")
print(f"O numero de erros foi {erro}")

print("Obrugado por estudar conosco, foi um prazer ter você por aqui!!")
print("FIM")


            
            

        
            
            


    