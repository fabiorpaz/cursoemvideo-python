print(f'{" Loja dos Reis ":=^40}')  #o "^" centraliza a frase em 40 espaços
preco = float(input('Preço do produto: R$ '))
condicao = float(input('Forma de pagamento:\n '
                       '- [1] A vista em dinheiro :\n '
                       '- [2] A vista com cartão de débito/crédito :\n '
                       '- [3] Parcelado no cartão de crédito :\n '
                       '- Digite a opção de pagamento: '))
if condicao == 1:
    total = preco - (preco * 10 / 100)
    print(f'Forma de pagamento: À VISTA EM DINHEIRO\n '
          f'Total a vista com 10% de desconto: {total:.2f}')
elif condicao == 2:
    total = preco - (preco * 5 / 100)
    print(f'Forma de pagamento: À VISTA com CARTÃO DE CRÉDITO/DÉBITO\n '
          f'Total a vista com 5% de desconto: {total:.2f}')
elif condicao == 3:
    total = preco
    parcela = int(input('Digite a quantidade de parcelas: '))
    if preco < 20.00 and parcela >= 2:
        print('Não é possível parcelar valores menores de R$ 20.00')
    elif parcela == 2:
        total_parc = preco / parcela
        print(f'Quantidade de parcelas: {parcela}\n'
              f'Valor total das parecelas S/ ACRÉSCIMO: {total_parc:.2f}')
    elif parcela >= 3:
        preco = 20 * preco / 100 + preco
        total_parc = preco / parcela
        print(f'{parcela}x com 20% DE ACRÉSCIMO: {parcela}x de R${total_parc:.2f}\n '
              f'Valor total com acréscimo: R${preco:.2f}')
    elif parcela == 1:
        total = preco - (preco * 5 / 100)
        print(f'Forma de pagamento: À VISTA com CARTÃO DE CRÉDITO/DÉBITO\n '
              f'Total a vista com 5% de desconto: {total:.2f}')
    elif parcela == 0:
        print('REINICIE O PROGRAMA E INSIRA UM VALOR VÁLIDO')
else:
    print('OPÇÃO INVÁLIDA. REINICIE O PROGRAMA')

