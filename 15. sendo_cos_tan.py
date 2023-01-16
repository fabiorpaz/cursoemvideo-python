import math
angulo = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print(f'O seno de {angulo}º é {sen:.2f}, seu cosseno é {coss:.2f} e sua tangente é {tang:.2f}')