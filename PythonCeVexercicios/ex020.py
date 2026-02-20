# SORTEANDO ORDEM DOS TRABALHOS #

import os
from random import shuffle

nome_programa = 'ordenando alunos'

os.system('cls')
print(50 * '=')
print('{:^50}'.format(nome_programa.upper()))
print(50 * '=')

quant_alunos = int(input('Quantos alunos irão participar do sorteio ? '))

lista_alunos = []

for i in range(quant_alunos):
    lista_alunos.append(input('Digite o nome do {}º aluno: '.format(i+1)))

shuffle(lista_alunos)

print('A ordem de apresentação dos alunos será: {}'.format(lista_alunos))