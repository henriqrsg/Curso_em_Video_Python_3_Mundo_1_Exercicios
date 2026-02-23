# JOGO DE ADIVINHAÇÃO #

import random 

import os

num = random.randint(0, 5)

nome_programa = 'VAMOS TESTAR SUA SORTE'

def interface():
    os.system('cls')
    print(70 *  '=')
    print('{:^70}'.format(nome_programa.upper()))
    print(70 *  '=')
    numero_escolhido = int(input('Escolha um número entre 0 e 5: '))
    return numero_escolhido

numero_escolhido = interface()

if numero_escolhido == num:
    print('\033[1;32mParabéns! Você acertou o número!\033[m')
else:
    print('\033[1;31mPoxa! Você errou! O número escolhido foi o {} e não o {}\033[m.'.format(num, numero_escolhido))
