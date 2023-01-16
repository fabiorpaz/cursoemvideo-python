dias = int(input('Quantos dias foram alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R$ {pago:.2f}')