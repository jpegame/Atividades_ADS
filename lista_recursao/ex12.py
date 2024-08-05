'''Defina uma função recursiva que recebe como argumento uma lista de listas de
números inteiros w e devolve True se em todas as sublistas de w existir um número
positivo. Por exemplo, no caso da lista [[2,4,3,1],[3,-5,-7],[],[8,0,-6]] a função deve
devolver False porque em [] não existe nenhum número positivo.'''

def existePositivo(lista):
    primeira_sublista, *resto_sublistas = lista
    for numero in primeira_sublista:
        if numero > 0:
            if len(resto_sublistas) == 0:
                return True
            return existePositivo(resto_sublistas)

    return False 

def main():
    lista = [[2,4,3,1],[3,-5,-7],[-1],[8,0,-6]]
    if existePositivo(lista):
        print('Todos as sub-listas possuem números positivos.')
    else:
        print('Pelo menos uma lista não possui um número positivo.')

main()