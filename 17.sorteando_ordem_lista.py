from time import sleep
from random import shuffle
#sample([aluno1, aluno2, aluno3, aluno4], k=2)  -> serão escolhidos 2 dentre os 4 alunos

print('Olá professor!! Digite o nome dos alunos a serem sorteados conforme solicitado abaixo:\n')

n1 = (input('Digite o nome do PRIMEIRO aluno: '))
n2 = (input('Digite o nome do SEGUNDO aluno: '))
n3 = (input('Digite o número do TERCEIRO aluno: '))
n4 = (input('Digite o nome do QUARTO aluno: '))

lista = [n1, n2, n3, n4]
shuffle(lista)
sleep(1.5)

print(f'A ordem de apresentação do trabalho será: {lista}.')
