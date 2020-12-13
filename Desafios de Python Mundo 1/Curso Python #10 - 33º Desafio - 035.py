print('='*20)
print('Analisador de Triângulo.')
print('='*20)
reta1 = float(input('Qual o comprimento da primeira reta? '))
reta2 = float(input('Qual o comprimento da segunda reta? '))
reta3 = float(input('Qual o comprimento da terceira reta? '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os três valores formam um triângulo.')
else:
    print('Os três valores não formam um triângulo.')
