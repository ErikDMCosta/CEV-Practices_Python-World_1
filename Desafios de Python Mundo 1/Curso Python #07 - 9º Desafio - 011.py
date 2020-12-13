Largura = float(input('Qual é a largura da parade a ser pintada? '))
Altura = float(input('Qual é a altura da parede a ser pintada? '))
Area = Largura * Altura
print('A parede tem a dimensão de {}x{} e a sua área é de {}m²'.format(Largura,Altura,Area))
Tinta = Area / 2
print('Para printar está parede você prescisará de {}l de tinta'.format(Tinta))