#13- FAÇA UM ALGORÍTIMO QUE LEIA O SALÁRIO DE UM FUNCIONÁRIO E MOSTRE SEU NOVO SALÁRIO COM 15% DE AUMENTO.

nome = input('Qual o nome do funcionário? ')
salario = float(input(f'Qual o salário atual de {nome}? '))
aumento = salario * 0.15 #multiplicar por 0.15 é o mesmo que dividir 15/100 para o aumento de 15%
print(f'O salário atual de {nome} é R$ {salario:.2f} e com o aumento de 15% irá para R$ {salario+aumento:.2f}!')
