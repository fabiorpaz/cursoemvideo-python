from random import randint

computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? '))

if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('PARABENS! Voce conseguiu me vencer!')