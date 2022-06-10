'''print('=' * 50)

co = float (input("Comprimento do cateto oposto "))
ca = float (input("Comprimento do cateto adjacente "))
hi = (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa vai medir {:.2f}" .format(hi))

print('=' * 50)'''

print('=' * 50)

from math import hypot
co = float (input("Comprimento do cateto oposto "))
ca = float (input("Comprimento do cateto adjacente "))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}', hi))

