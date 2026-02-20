# PARTE INTEIRA DO NÚMERO #

from math import trunc

numero = float(input('Digite um número: '))

print ('A parte inteira do número {:.4f} é {}'.format(numero, trunc(numero)))