'''
Uma indústria de alimentos congelados tem capacidade para estocar até 5 toneladas
de produto pronto para venda. Faça um programa que controle o estoque dessa
empresa, lendo do teclado a produção em kg de cada dia (sendo que uma produção
igual a zero é utilizada para encerrar a leitura).

'''

estoque = 0
capacidade = 5000

print("Controle de estoque de alimentos congelados")
print("Digite os valores em Kg.(Caso queira encerrar o programa digite: 0")

while True:
    producao_dia = float(input("Digite o valor da produção do dia em Kg: "))

    if producao_dia == 0 or producao_dia > 5000:
        break

    estoque += producao_dia

    if estoque == 2500:
        print("Metade do seu estoque esta disponivel")
    elif estoque > 5000:
        print("ATENÇÃO!! O limite do estoque foi atingido!")
        break

if producao_dia > 5000:
    print("ATENÇÃO!! Valor maior que o espaço do estoque")
else:
    print(f"Espaço do estoque consumido atualmente: {estoque}Kg")
    



    
