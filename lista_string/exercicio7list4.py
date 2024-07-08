texto = []

while True:
    linha = input()
    if linha == " ":
        break 
    texto.append(linha)
numero_caracter = numero_espacos = 0
numero_linhas = len(texto)
for linha  in texto:
    numero_caracter += len(linha)
    numero_espacos += linha.count(" ")

print("\nTexto digitado: ")
for linha in texto:
    print(linha)
print("\nEstatísticas do texto:")   
print(f"O número de caracteres digitados no texto foi: {numero_caracter}") 
print(f"O número de espaços digitados no texto foi: {numero_espacos}")
print(f"O número de linhas do texto foi: {numero_linhas}")