"""Escreva uma função recursiva que, dada uma string s e um caractere c, conte o
número de ocorrências do caractere c na string s."""

def contar_ocorrencia(s,c):
    if not s:
        return 0
    elif s[0] == c:
        return 1 + contar_ocorrencia(s[1:],c)
    else:
        return contar_ocorrencia(s[1:],c)
    
def main():
    string = input("Digite a string: ").strip().lower()
    print("-="*30)
    caractere = input("Digite o caractere: ").strip().lower()

    while len(caractere) != 1:
        caractere = input("Digite apenas um caractere: ")

    print("-="*30)
    print(f"O caractere '{caractere}' ocorre {contar_ocorrencia(string, caractere)} vezes na string '{string}'.")

main()
