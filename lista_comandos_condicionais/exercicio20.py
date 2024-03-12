custo_operacao = float(input('Custo da operação em R$:'))
escolha_conversao = int(input(
    """
    Escolha a moeda para conversão:
    1 - Dólar Americano
    2 - Euro
    3 - Libra esterlina
    4 - Yuan
    """
))

if escolha_conversao == 1:
    print('Conversão para dólar: ', custo_operacao * 3.258)
elif escolha_conversao == 2:
    print('Conversão para euro: ', custo_operacao * 4.095)
elif escolha_conversao == 3:
    print('Conversão para libra esterlina: ', custo_operacao * 4.529)
elif escolha_conversao == 4:
    print('Conversão para yuan: ', custo_operacao * 0.515)
else:
    print('Escolha inválida')