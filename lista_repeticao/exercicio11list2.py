"""
O volume de uma esfera pode ser calculado pela fórmula
3
3
4
V = r
, onde r é o raio da
esfera. Faça um programa que imprima uma tabela de volumes para esferas que
tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm. 
"""

import math


print("---------------------------")
print("   Raio     |    Volume     ")
print("---------------------------")

raio = 0.0

while raio <= 15.0:
    vol = (4/3) * math.pi * raio**3
    print(f"   {raio:.2f}     |    {vol:.2f}     ")
    raio += 0.5