from random import choice
N1 = str(input('Primeiro aluno: '))
N2 = str(input('Segundo aluno: '))
N3 = str(input('Terceiro aluno :'))
N4 = str(input('Quarto aluno: '))
Lista = [N1, N2, N3, N4]
Resultado = choice(Lista)
print('O Aluno sorteado foi {}'.format(Resultado))
