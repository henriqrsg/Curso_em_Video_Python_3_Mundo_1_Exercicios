# CALCULO DE MULTA #

import os

nome_programa = 'verificando a velocidade'

def interface ():
    os.system('cls')
    print(50 * '\033[1;36m=\033[m')
    print('\033[1;36m{:^50}\033[m'.format(nome_programa.upper()))
    print(50 * '\033[1;36m=\033[m')
    print('')
interface()

velocidade = int(input('Qual a velocidade que você esta dirigindo seu carro ? [Km/h]: '))

velocidade_maxima = 80

diferenca_velocidade = velocidade - velocidade_maxima

multa = 15

valor_multa = diferenca_velocidade * multa

if velocidade > velocidade_maxima:
    print('\033[1;31mVocê está dirigindo á {}km/h a mais que a velocidade permitida! Portanto você sera multado em R$ {:.2f}!\033[m'.format(diferenca_velocidade, valor_multa))
else:
    print('\033[1;32mParabéns! Você não foi multado! Continue dirigindo corretamente!\033[m')