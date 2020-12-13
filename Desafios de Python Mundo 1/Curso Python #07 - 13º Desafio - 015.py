DIAS = int(input('Qual a quantidade de dias pelos quais ele foi alugado? '))
KM = float(input("Qual a quantidade de Km percorridos por um carro alugado? "))
PAGO = (DIAS * 60) + (KM * 0.15)
print('O valor total a ser pago é de R${:.2f}'.format(PAGO))

