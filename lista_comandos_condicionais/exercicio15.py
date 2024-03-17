'''
Construa um programa que receba três valores quaisquer e imprima-os em ordem
crescente. Como seu programa reage a valores de entrada iguais como no exercício
anterior? 
'''
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))
if num1 > num2 > num3:
    print(f"{num3} - {num2} - {num1}")
elif num1 > num3 > num2:
    print(f"{num2} - {num3} - {num1}")
elif num2 > num3 > num1:
    print(f"{num1} - {num3} - {num2}")
elif num2 > num1 > num3:
    print(f"{num3} - {num1} - {num2}")
elif num3 > num2 > num1:
    print(f"{num1} - {num2} - {num3}")
elif num3 > num1 > num2:
    print(f"{num2} - {num1} - {num3}")
elif num1 == num2 > num3:
    print(f"{num3} - {num2} - {num1}")
elif num1 == num2 < num3:
    print(f"{num1} - {num2} - {num3}")
elif num2 == num3 > num1:
    print(f"{num1} - {num2} - {num3}")
elif num2 == num3 < num1:
    print(f"{num3} - {num2} - {num1}")
else:
    print(f"{num1} - {num2} - {num3}")


print("Fim")



    
