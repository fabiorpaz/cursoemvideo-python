from datetime import date

atual = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Este ano é o seu ano de alistamento')
elif idade < 18:
    saldo = 18-idade
    print(f'Ainda faltam {saldo} anos para o alistamento militar')
    ano = atual+saldo
    print(f'Seu alistamento será em {ano}')
else:
    saldo = idade-18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    ano = atual-saldo
    print(f'Seu alistamento foi em {ano}')