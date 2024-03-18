"""
Em um cinema que possui capacidade de 50 lugares foi distribuído um questionário
aos expectadores, no qual constava a idade e a sua opinião em relação ao filme,
segundo: ótimo, bom, regular, ruim ou péssimo. Elabore um programa que, lendo
estes dados, de diversos espectadores (até o limite de capacidade do cinema) calcule
e imprima:
a. A quantidade de respostas ótimo, bom, regular, ruim e péssimo.
b. A percentagem de ótimo, bom, regular, ruim e péssimo.
c. A idade do mais velho entrevistado.
d. A idade do mais novo entrevistado.
"""

otimo = 0
bom = 0
regular = 0
ruim = 0
pessimo = 0
idades = []
capacidade = int(input("Digite o numero de questionários distribuídos nesta sessão: "))
if capacidade > 50:
    print("O limite de questionários entregues é 50")

for i in range(capacidade):

    idade = int(input("Digite sua idade: "))
    print("Qual sua opinião sobre o filme?",end="\n")
    opiniao = input("Ótimo - bom - regular - ruim - péssimo: ")

    idades.append(idade)
    if opiniao == "Ótimo":
        otimo += 1
    elif opiniao == "Bom":
        bom += 1
    elif opiniao == "Regular":
        regular += 1
    elif opiniao == "Ruim":
        ruim += 1
    elif opiniao == "Péssimo":
        pessimo += 1


idade_mais_velho = max(idades)
idade_mais_novo = min(idades)

questi_total = otimo + bom + regular + ruim + pessimo

porcen_otimo = (otimo/questi_total) * 100
porcen_bom = (bom/questi_total) * 100
porcen_regular = (regular/questi_total) * 100
porcen_ruim = (ruim/questi_total) * 100
porcen_pessimo = (pessimo/questi_total) * 100


print(end="\n\n")
print("Quantidade de respostas:")
print("Ótimo:", otimo)
print("Bom: ", bom)
print("Regular: ",regular)
print("Ruim: ", ruim)
print("Péssimo: ",pessimo)
print(end="\n\n")

print("Porcentagem de cada resposta:")
print("Ótimo: ",porcen_otimo,"%")
print("Bom: ", porcen_bom,"%")
print("Reguler: ", porcen_regular,"%")
print("Ruim: ", porcen_ruim,"%")
print("Péssimo: ", porcen_pessimo,"%")



print("A idade do mais velho é: ", idade_mais_velho , "Anos")

print("A idade do mais novo é: ", idade_mais_novo, "Anos") 