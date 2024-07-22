import math

# Função para converter graus em radianos
def graus_para_radianos(graus):
    return graus * (math.pi / 180)

# Função para calcular o seno usando a série de McLaurin
def seno_mc_laurin(graus, precisao):
    radianos = graus_para_radianos(graus)
    seno = 0
    for n in range(precisao):
        termo = ((-1)**n) * (radianos**(2*n + 1)) / math.factorial(2*n + 1)
        seno += termo
    return seno

# Programa principal de teste
def main():
    # Captura e valida a entrada do usuário
    angulo_str = input("Digite o ângulo em graus: ")
    precisao_str = input("Digite a precisão (número de termos da série): ")

    # Converte as entradas para os tipos apropriados
    angulo = float(angulo_str)
    precisao = int(precisao_str)

    # Verifica se a precisão é um número positivo
    if precisao <= 0:
        print("A precisão deve ser um número inteiro positivo.")
        return

    # Calcula o seno usando a série de McLaurin
    seno_calculado = seno_mc_laurin(angulo, precisao)
    seno_real = math.sin(graus_para_radianos(angulo))

    # Exibe os resultados
    print(f"\nÂngulo: {angulo} graus")
    print(f"Seno calculado (McLaurin): {seno_calculado:.2f}")
    print(f"Seno real (math.sin): {seno_real:.2f}")

main()