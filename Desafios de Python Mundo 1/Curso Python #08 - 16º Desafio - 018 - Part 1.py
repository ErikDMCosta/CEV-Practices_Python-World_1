import math
ang = float(input('Digite o valor do angulo desejado :'))
seno = math.sin(math.radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
coseno = math.cos(math.radians(ang))
print('O angulo de {} tem CONSENO de {:.2f}'.format(ang, coseno))
tangente = math.tan(math.radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))


