dia1=int(input("Digite dia1: "))
mes1=int(input("Digite mes1: "))
ano1=int(input("Digite ano1 "))

dia2=int(input("Digite dia2: "))
mes2=int(input("Digite mes2: "))
ano2=int(input("Digite ano2: "))

if ano1 > ano2:
    print("A data 2 ocorreu cronológicamente primeiro")
elif ano1 < ano2:
    print("A data 1 ocorreu cronológicamente primeiro")
else:
    if mes1 > mes2:
        print("A data 2 ocorreu cronológicamente primeiro")
    elif mes1 < mes2:
        print("A data 1 ocorreu cronológicamente primeiro")
    else:
        if dia1 > dia2:
            print("A data 2 ocorreu cronológicamente primeiro")
        elif dia1 < dia2:
            print("A data 1 ocorreu cronológicamente primeiro")
        else:
            print("As datas ocorreram juntas cronológicamente")

print("Fim")