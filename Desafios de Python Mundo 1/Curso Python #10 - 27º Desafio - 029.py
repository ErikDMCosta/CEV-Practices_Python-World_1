vel = float(input('Qual é a atual velocidade do carro? '))
if vel > 80:
    print('Você foi multado por ultrapassar a velocidade permitida dos 80 KM/h')
    res = (vel - 80) * 7
    print('O valor da multa será de R${:.2f}.'.format(res))
    print('Na próxima tenha mais cuidado além da lei pode estar colocando sua vida ou de outros em risco!')
else:
    print('Você não foi multado, pois está dirigindo na velocidade permitida.')
    print('Tenha um bom dia! Dirija com segurança!')