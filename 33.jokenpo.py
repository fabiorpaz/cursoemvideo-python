from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
(sleep)
print('-=-'*11)
print(f'Computador jogou {(itens[computador])}')
print(f'Você jogou {(itens[jogador])}')
print('-=-'*11)

if computador == 0: #computador jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence') 
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Opção de jogada inválida')
if computador == 1: #computador jogou Papel
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')   
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Opção de jogada inválida')
if computador == 2: #computador jogou Tesoura
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Opção de jogada inválida')