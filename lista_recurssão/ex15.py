"""Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve True se cada lista em w tiver igual número de
elementos positivos e negativos, e False em caso contrário. Por exemplo, no caso da
lista [[2,4,-3,-1],[-3,0,7],[-8,6]] a função deve devolver True pois todas as listas têm
igual número de elementos positivos e negativos."""

def contar_positivos_negativos(sublista):
    positivos = sum(1 for num in sublista if num > 0)
    negativos = sum(1 for num in sublista if num < 0)
    return positivos, negativos

def verifica_listas_iguais(w):
    if not w:
        return True
    else:
        sublista = w[0]
        positivos, negativos = contar_positivos_negativos(sublista)
        if positivos != negativos:
            return False
        else:
            return verifica_listas_iguais(w[1:])

def obter_lista_usuario():
    lista_principal = []
    while True:
        entrada = input("Digite uma sublista de números inteiros separada por vírgulas (ou apenas pressione Enter para finalizar): ")
        if entrada.strip() == "":
            break
        sublista_str = entrada.split(',')
        try:
            sublista = [int(num) for num in sublista_str]
            lista_principal.append(sublista)
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar uma lista de números inteiros separados por vírgulas.")
    
    return lista_principal

def main():
    lista_usuario = obter_lista_usuario()
    resultado = verifica_listas_iguais(lista_usuario)
    print("Resultado da verificação:", resultado)

main()
