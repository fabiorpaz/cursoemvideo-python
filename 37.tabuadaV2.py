num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} X {c:2} = {num*c}') #":2" é referente ao espaço de casas que o termo ocupa.