r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima podem formar um triângulo',  end='')
    if r1 == r2 == r3:
        print(' EQUILATERO!')
    if r1 != r2 != r3 != r1:
        print(' ESCALENO')
    if r1 == r2 != r3 or r2 == r3 != r1 or r1 == r3 != r2:
        print(' ISOSCELES!')
else:
    print('Não podem formar um triângulo!')