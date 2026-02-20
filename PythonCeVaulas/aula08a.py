import math

numero = int(input('Digite um número: '))

print('A raiz quadrada do número {} é {:.2f}'.format(numero, math.sqrt(numero)))

# ou #

from math import sqrt

numero = int(input('Digite um número: '))

print('A raiz quadrada do número {} é {:.2f}'.format(numero, sqrt(numero)))

import random

aleatorio = random.randint(1, 10)

print(aleatorio)

import emoji 

print(emoji.emojize('Oohh my gooo 😱'))