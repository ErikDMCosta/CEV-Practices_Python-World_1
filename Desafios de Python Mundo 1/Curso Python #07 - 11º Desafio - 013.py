NS = float(input('Digite o valor do seu salário para descobrir como será com seu aumento: '))
NNS = NS+(NS*15/100)
print('O seu salário atual é de R${:.2f}, mas com o aumento de 15% será de R${:.2f}'.format(NS, NNS))

