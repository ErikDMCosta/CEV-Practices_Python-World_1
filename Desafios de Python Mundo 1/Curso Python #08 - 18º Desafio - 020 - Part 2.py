from random import shuffle
N1 = str(input('Nome do primeiro aluno: '))
N2 = str(input('Nome do segundo aluno:'))
N3 = str(input('Nome do terceiro aluno:'))
N4 = str(input('Nome do quarto aluno: '))
Cadeia = [N1,N2,N3,N4]
Resultado = shuffle(Cadeia)
print('A lista dos nome sorteados em ordem é de {}.'.format(Cadeia))



