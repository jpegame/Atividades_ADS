def e_numero_real(valor):

    if not valor:
        return False
    if valor[0] == '-' and len(valor) > 1:  # Permite números negativos
        valor = valor[1:]
    partes = valor.split('.')
    if len(partes) > 2:  # Mais de um ponto decimal
        return False
    for parte in partes:
        if not parte.isdigit():  # Verifica se cada parte é composta apenas por dígitos
            return False
    return True

def receber_valores_reais():
    while True:
        entrada = input("Digite os valores reais separados por espaços ou vírgulas: ").strip()
        # Substitui as vírgulas por espaços para uniformizar a divisão
        entrada = entrada.replace(',', ' ')
        # Divide a string de entrada em uma lista de substrings
        substrings = entrada.split()

        valores_reais = []
        valido = True
        
        for substring in substrings:
            if e_numero_real(substring):
                valores_reais.append(float(substring))
            else:
                valido = False
                print(f"Valor inválido encontrado: {substring}")
                break

        if valido:
            return valores_reais
        else:
            print("Entrada inválida. Certifique-se de que todos os valores são números reais e tente novamente.")

def calcular_media(valores):
    if len(valores) == 0:
        return None
    return sum(valores) / len(valores)

def encontrar_maior(valores):
    if len(valores) == 0:
        return None
    return max(valores)

def encontrar_menor(valores):
    if len(valores) == 0:
        return None
    return min(valores)

def calcular_soma(valores):
    return sum(valores)

def main():
    valores_reais = receber_valores_reais()

    print(f"Os valores inseridos são: {valores_reais}")
    print("-="*30)
    print(f"Média dos valores: {calcular_media(valores_reais)}")
    print("-="*30)
    print(f"Maior valor: {encontrar_maior(valores_reais)}")
    print("-="*30)
    print(f"Menor valor: {encontrar_menor(valores_reais)}")
    print("-="*30)
    print(f"Soma dos valores: {calcular_soma(valores_reais)}")


main()
