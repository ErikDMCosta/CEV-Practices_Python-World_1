num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
if num1 < num2 and num1 < num3:
    menor = num1
    print('Menor numero é {}.'.format(menor))
if num2 < num3 and num2 < num1:
    menor = num2
    print('Menor numero é {}.'.format(menor))
if num3 < num1 and num3 < num2:
    menor = num3
    print('Menor numero é {}.'.format(menor))
if num1 > menor and num1 > num2 and num1 > num3:
    print('Maior numero é {}.'.format(num1))
if num2 > menor and num2 > num1 and num2 > num3:
    print('Maior numero é {}.'.format(num2))
if num3 > menor and num3 > num1 and num3 > num2:
    print('Maior numero é {}.'.format(num3))
else:
    print('Programa encerrado!.')
