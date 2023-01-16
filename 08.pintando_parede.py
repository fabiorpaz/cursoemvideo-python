larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt
print(f'sua parede tem a dimensao de {larg} X {alt} e sau area é de {area}m².')
tinta = area/2 #2 é a quantidade gasta de tinta por m²
print(f'para pintar essa parede, voce precisará de {(tinta):.0f}L de tinta') #(:.0f) para nao ter casa decimal. outra opcao seria colocar "int(tinta)