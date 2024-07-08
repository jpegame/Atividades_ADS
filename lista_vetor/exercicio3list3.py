numeros = []
for i in range (15):
    num = float(input(f"Digite o {i+1}° valor: "))
    if num < 0:
        print("Ops, você digitou um número negativo!"),print("Digite apenas números positivos")
        break
    numeros.append(num)
media = sum(numeros)/15
print("=-"*30)
print(f"A média dos valores digitados é {media:.2f}"),print("-"*30)
print("Os números digitados abaixo da média são: ")
for c in numeros:
    if c < media:
        print(c,end=" - ")
print("FIM")
