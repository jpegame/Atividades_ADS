'''
25. Foi realizada uma pesquisa de algumas características físicas da população de uma
certa região, a qual foram coletados os seguintes dados referentes a cada habitante
para serem analisados:
• Sexo.
• Cor dos olhos (azuis, verdes, castanhos).
• Cor dos cabelos (louros, castanhos, pretos).
• Idade.
Faça um programa que determine e escreva:
a. O total de entrevistados
6
b. O total de homens e o total de mulheres entrevistados
c. A maior e a menor idade do conjunto de habitantes;
d. A média de idade do conjunto de habitantes;
e. A percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35
anos inclusive e que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido pelo valor -1 para a idade.
'''



t_entrevistados = 0
t_homens = 0
t_mulheres = 0
soma_idade = 0
mulheres_x_caracteristicas = 0
maior = 0
menor = 150
while True:

    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo == "F":
        t_mulheres += 1
    else:
        t_homens += 1
    
    idade = int(input("Qual a sua idade?: "))
    if idade > maior:
        maior = idade

    if idade < menor:
        menor = idade

    soma_idade += idade

    cor_olhos = input("Indique a cor dos seus olhos (A - Azul; B - Verde; C- Pretos): ").upper()
    
    cor_cabelo = input("Indique a cor do seu cabelo. (A - Louros; B - Castanhos; C - Pretos): ").upper()

    if idade >= 18 and idade <= 35 and cor_olhos == "B" and cor_cabelo == "A":
        mulheres_x_caracteristicas +=1

    t_entrevistados += 1

    continuar = input("Deseja coletar dados de mais um habitante? (S/N): ").upper()
    if continuar == "N":
        break

media_idade = soma_idade/t_entrevistados
porcentagem_mulheres_x_caracteristicas = (mulheres_x_caracteristicas/t_mulheres)*100

print("------Resultados-------")
print(f"Número total de entrevistados: {t_entrevistados}")
print(f"Número de homens entrevistados: {t_homens}")
print(f"Número total de mulheres entrevistadas: {t_mulheres}")
print(f"A menor e a maior idade do conjunto de habitantes: {menor} e {maior}")
print(f"A média de idade do conjunto de habitantes: {media_idade:.2f}")
print(f"Porcentagem de mulheres cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos louros: {porcentagem_mulheres_x_caracteristicas:.2f}%")

    

