preco = float(input('qual o preço do seu produto? R$ '))
preco_atualizado = preco - (preco * 5/100) #desconto de 5%
print(f'o produto que custava R$ {preco:.2F}, na promoção sairá por R$ {preco_atualizado}')
