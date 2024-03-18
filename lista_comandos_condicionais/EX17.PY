"""
17. Escreva um programa que leia os três lados de um triângulo e imprima se o triângulo
é equilátero, isósceles ou escaleno, ou ainda, se estes lados não podem constituir um
triângulo.
Lembre-se que:
• O comprimento de cada lado de um triângulo é sempre menor do que a soma
dos comprimentos dos outros dois lados.
• Triângulo equilátero: três lados iguais.
• Triângulo isósceles: dois lados iguais.
• Triângulo escaleno: três lados diferentes
"""
#Comecei pedindo para a pessoa apresentar os valores dos lados do triângulo
Lado1 = float(input("Informe o primeiro lado do triângulo: "))
Lado2 = float(input("Informe o segundo lado do triângulo: "))
Lado3 = float(input("Informe o terceiro lado do triângulo: "))

#Depois chequei se o triângulo pode existir, se sim, qual o tipo do triângulo
if Lado1 < Lado2 + Lado3 and Lado2 < Lado1 + Lado3 and Lado3 < Lado1 + Lado2:
    if Lado1 == Lado2 == Lado3: 
        print("Triangulo_Equilatero")
    elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
        print("Triangulo_Isosceles")
    elif Lado1 != Lado2 != Lado3:
        print("Triangulo_Escaleno")
else:
    print("Esse triângulo não existe")

    
