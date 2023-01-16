soma = 0
cont = 0
for c in range (1, 501, 2):
    print(c, end= ' ')
    if c%3 == 0:
        soma += c        #soma = soma + c
        cont += 1        #cont = cont + 1

print('\n'f'A soma de todos os {cont} valores solicitados é {soma}')