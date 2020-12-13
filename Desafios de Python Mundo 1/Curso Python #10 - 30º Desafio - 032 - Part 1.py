ano = int(input('Que ano quer analisar?'))
if ano % 4 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÂO é BISSEXTO.'.format(ano))
