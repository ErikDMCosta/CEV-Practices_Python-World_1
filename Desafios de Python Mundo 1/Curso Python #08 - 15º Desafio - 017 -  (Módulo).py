import math
CCO = float(input('Digite o comprimento do Cateto Oposto: '))
CCA = float(input('Digite o cateto adjacente : '))
HI = math.hypot((CCO, CCA))
print('A hipotenusa vai medir {:.2f}'.format(HI))
