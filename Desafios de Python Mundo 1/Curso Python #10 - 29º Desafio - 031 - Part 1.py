val = float(input('Qual é a distância da viagem em KM ?'))
if val <= 200:
    calc = val * 0.50
    print('A distância e inferior a 200 KM, portanto o valor será de R${:.2f}'.format(calc))
else:
    calc = val * 0.45
    print('A distância e superior a 200 KM, portanto o valor será de R${:.2f}'.format(calc))
