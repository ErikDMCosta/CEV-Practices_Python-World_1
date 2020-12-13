import random
num = int(input('Digite um numero inteiro de 0 a 5: '))
ram = random.randint(0, 5)
if num == ram:
    print('Você venceu!')
    print('Acertou o numero aleatório sorteado pela máquina. PARABÉNS!')
else:
    print('O computador venceu !')
    print('Errou o numero sorteado pela máquina, não foi desta vez.')

