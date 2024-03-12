n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))
n3 = int(input('Digite um número:'))

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(n3,n2,n1)
        else:
            print(n2,n3,n1)
    else:
        print(n2,n1,n3)
elif n2 > n3:
    if n1 > n3:
        print(n3,n1,n2)
    else: 
        print(n1,n3,n2)
else:
    print(n1,n2,n3)