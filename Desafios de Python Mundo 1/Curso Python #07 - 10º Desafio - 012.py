V = float(input('Qual o valor do produto em liquidação com 5 % de desconto?'))
Promo = V-(V*5/100)

print('O produto que custava R${:.2f}, na promoção de desconto de 5% vai custar R${}'.format(V, Promo))


