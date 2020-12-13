val = float(input('Qual é a distância da viagem em KM ?'))
calc = val * 0.50 if val <= 200 else val * 0.45
print('A distância é de {} KM, portanto o valor será de R$ {:.2f}'.format(val,calc))


