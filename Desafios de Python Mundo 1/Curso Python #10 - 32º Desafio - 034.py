cont = float(input('Qual é o valor do seu salário atual em R$?  '))
val = 1250
if cont <= val:
    calc = cont + (val * 15 / 100)
    print('Seu salario é de R$ {} e o aumento será de R${:.2f}.'.format(cont,calc))
else:
    calc = cont + (val * 10 / 100)
    print('Seu salario é de R$ {} e o aumento será de R${:.2f}.'.format(cont,calc))


