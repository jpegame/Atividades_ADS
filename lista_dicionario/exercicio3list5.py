string = input("Digite uma string: ")
contagem_caracteres = {}
for caractere in string:
    if caractere in contagem_caracteres: 
        contagem_caracteres[caractere] += 1 
    else:
        contagem_caracteres[caractere] = 1 

num_unico_carac = len(contagem_caracteres)
print(f"O número de carácters únicos da string {string} é {num_unico_carac} ")

