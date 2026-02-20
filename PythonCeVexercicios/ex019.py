# SORTEANDO UM DOS ALUNOS #

import os

from random import choice

nome_programa = 'sorteando alunos'

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa.upper()))
    print(50 * '=')

def sorteando():
    try:
        quant_alunos = int(input('Digite quantos alunos irão participar do sorteio [1] [2] [3] ... : '))
        return quant_alunos
    except ValueError:
        print('Digite apenas números por favor!')
        return sorteando()

interface()
quant_alunos = sorteando()

if quant_alunos <= 0:
    print('Poxa meu amigo, não é possível realizar o sorteio com {} alunos =('.format(quant_alunos))
else:
    for i in range (quant_alunos):
        lista_alunos = []
        lista_alunos.append(input('digite o nome do {}º aluno: '.format(i+1)))
    aluno_sorteado = choice(lista_alunos)
    print('O aluno sorteado foi {}'.format(aluno_sorteado))