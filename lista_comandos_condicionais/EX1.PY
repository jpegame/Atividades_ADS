"""
1.Um shopping está fazendo uma promoção na qual o cliente que fizer compras de
valor até R$100,00 ganha um cupom para concorrer a um carro e se ele comprar
acima de R$100,00 ganha dois cupons e um vale-desconto no total de 10% da
compra. Faça um programa que leia do teclado o total de compras e imprima se o
cliente tem direito a 1 cupom, ou a 2 cupons e o vale-desconto (nesse caso, imprima
o valor do desconto). Declare como constantes simbólicas o limite e o percentual do
desconto.
"""
#Constantes simbólicas
Limite_Promoçao = 100
Desconto_Porcentual = 10

# Declarei varáveis para o quanto a pessoa gastou e a porcentagem aplicada sobre esse valor
Valor = float(input("Informe o valor da sua compra: R$"))
Desconto = Valor *  (Desconto_Porcentual/100)

# Aqui verifica a condição da promoção e exibe os resultados
if Valor <= Limite_Promoçao:
    print("Você ganhou um cupom para concorrer a um carro!")
elif Valor> Limite_Promoçao:
    print(f"Você ganhou dois cupons para concorrer a um carro, e ainda ganhou R${Desconto:.2f} de desconto!") 

