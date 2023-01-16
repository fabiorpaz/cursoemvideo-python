n = int(input('Digite um número para ver sua tabuada: '))
# se usar f com três aspas simples não precisa escrever tantos prints pois ele comporta diversas linhas
print(
    f'''
    {n} x {1:2} = {n*1} 
    {n} x {2:2} = {n*2}
    {n} x {3:2} = {n*3}
    {n} x {4:2} = {n*4}
    {n} x {5:2} = {n*5}
    {n} x {6:2} = {n*6}
    {n} x {7:2} = {n*7}
    {n} x {8:2} = {n*8}
    {n} x {9:2} = {n*9}
    {n} x {10:2} = {n*10}
    ''') #":2" é o mesmo que dizer para usar dois digitos. Por isso o espaço na execuçao do codigo

