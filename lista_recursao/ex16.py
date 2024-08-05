'''Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve o número de listas em w ordenadas por ordem
crescente em sentido lato, ou seja, em que cada elemento é menor ou igual que o
seguinte. Por exemplo, no caso da lista [[2,2,3,0],[1,2,5,4],[2,4,4]] a função deve
devolver 1 pois só a terceira lista está ordenada'''

def esta_ordenada(lista):
    '''Verifica a ordenação da lista com a lógica semelhante a função anterior'''
    if len(lista) == 1: # Se a lista tiver apenas um item ela então estará ordenada
        return True
    return lista[0] <= lista[1] and esta_ordenada(lista[1:])

def contar_listas_ordenadas(w):
    '''Faz a verificação do primeiro item passado em w (w[0]) e executa a mesma função para os outros items restantes, representado pelo w[1:]'''
    if not w: 
        return 0
    return (1 if esta_ordenada(w[0]) else 0) + contar_listas_ordenadas(w[1:])


def main():
    lista = [[2,2,3,0],[1,2,5,4],[2,4,4]]
    qtd_ordenada = contar_listas_ordenadas(lista)
    print(qtd_ordenada)

main()