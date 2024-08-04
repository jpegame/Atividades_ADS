'''Usando algoritmos recursivos, escreva funções que:
a. Obtenha o máximo de uma lista.
b. Obtenha o máximo de uma lista com n números.
c. Buscar um caractere c em uma string s a partir de uma posição index e retornar a
posição da primeira ocorrência deste caractere (caso encontre) ou −1 (caso
contrário).
'''

def max_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_restante = max_lista(lista[1:])
        return lista[0] if lista[0] > max_restante else max_restante

def max_lista_numeros(lista, n):
    if n == 1:
        return lista[0]
    else:
        max_restante = max_lista_numeros(lista, n-1)
        return lista[n-1] if lista[n-1] > max_restante else max_restante

def buscar_caractere(s, c, index=0):
    if index >= len(s):
        return -1
    elif s[index] == c:
        return index
    else:
        return buscar_caractere(s, c, index + 1)
    

def main():
    lista = [3, 5, 7, 2, 8]
    print(f"Valor máximo da lista: {max_lista(lista)}")

    # Exemplo b: Máximo de uma lista com n números
    n = len(lista)
    print(f"Máximo da lista {lista} com {n} números: {max_lista_numeros(lista, n)}")

    # Exemplo c: Buscar um caractere em uma string a partir de um índice
    string = "hello world"
    caractere = 'o'
    indice = 5
    print(f"Posição do caractere '{caractere}' na string '{string}' a partir do índice {indice}: {buscar_caractere(string, caractere, indice)}")

main()
