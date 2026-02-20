# JOGO DE ADIVINHAÇÃO #

import random 

num = random.randint(0, 5)

numero_escolhido = int(input('Escolha um número entre 0 e 5: '))

if numero_escolhido == num:
    print('\033[1;32mParabéns! Você acertou o número!\033[m')
else:
    print('\033[1;31mPoxa! Você errou! O número escolhido foi o {} e não o {}\033[m.'.format(num, numero_escolhido))