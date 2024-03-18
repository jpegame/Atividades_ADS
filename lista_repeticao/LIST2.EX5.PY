"""
5. Construir um programa que leia um conjunto de caracteres (uma frase, terminada por
“Enter”) da entrada padrão e ao final imprima o número de caracteres lidos.
"""

frase = input("Escreva uma frase: ")

n_caracteres = len(frase)  #"len" é uma função que define o número de itens de um objeto, no caso o numero de caracteres da frase

print(f"O número de caracteres é {n_caracteres}")