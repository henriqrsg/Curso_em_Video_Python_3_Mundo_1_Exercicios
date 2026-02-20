# VALORES SENO, COSSENO E TANGENTE #

import math

angulo = float(input('Digite um ângulo: '))

cosseno = math.cos(math.radians(angulo))
seno = math.sin(math.radians(angulo)) 
tangente = math.tan(math.radians(angulo))

print('O ângulo de {:.2f} graus tem seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(angulo, seno, cosseno, tangente))