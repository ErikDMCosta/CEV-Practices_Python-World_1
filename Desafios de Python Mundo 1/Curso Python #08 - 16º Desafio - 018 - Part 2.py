from math import radians, sin, cos, tan
ang = float(input('Digite o valor do angulo desejado :'))
seno = sin(radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, seno))
coseno = cos(radians(ang))
print('O angulo de {} tem CONSENO de {:.2f}'.format(ang, coseno))
tangente = tan(radians(ang))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tangente))


