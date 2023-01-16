from math import hypot

co = float(input('Comprimendo do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print(f'A hipotenusa vai medir {hi:.2f}')