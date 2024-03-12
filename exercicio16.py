a = float(input('Digite o valor de a:'))
b = float(input('Digite o valor de b:'))
c = float(input('Digite o valor de c:'))

x1 = 0
x2 = 0
delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print('Não existem raízes reais')
else:
    x1 = (-b + (delta)**(1/2)) / (2 * a)
    x2 = (-b - (delta)**(1/2)) / (2 * a)

print(f'x1: {x1} || x2: {x2}')