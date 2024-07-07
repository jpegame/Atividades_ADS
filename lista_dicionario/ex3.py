'''Faça um programa que conta quantos caracteres únicos existem em uma string. A
string 'Hello, world!' tem dez caracteres únicos, enquanto a string 'zzz' tem apenas
um. Utilize um dicionário para resolver esse problema'''

letras = {}
frase = input('Digite alguma coisa: ')
for i in frase: 
    letras[i] = True

print(f'O texto possui {len(letras)} caracteres únicos')