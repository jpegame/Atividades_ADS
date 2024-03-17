'''
Elabore um programa que dado o peso de um boxeador, informe à categoria a qual
pertence, seguindo a tabela abaixo.
Categoria Massa (Kg)
Palha < 50
Pluma < 59
Leve < 75
Pesado < 87
Super Pesado >= 87
'''

peso=float(input("Digite o seu peso: "))
if peso < 50:
    print("Sua categoria é Palha")
elif peso < 59:
    print("Sua categoria é Pluma")
elif peso < 75:
    print("Sua categoria é Leve")
elif peso < 87:
    print("Sua categoria é Pesado")
else:
    print("Sua categoria é Super Pesado")

print("fim")