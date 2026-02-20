# PODE FORMAR TRIÂNGULO #

primeiro_lado = int(input('Digite o comprimento do primeiro lado: '))
segundo_lado = int(input('Digite o comprimento do segundo lado: '))
terceiro_lado = int(input('Digite o comprimento do terceiro lado: '))

if primeiro_lado + segundo_lado < terceiro_lado or primeiro_lado + terceiro_lado < segundo_lado or segundo_lado + terceiro_lado < primeiro_lado:
    print('Os segmentos {}, {} e {} \033[1;31mnão podem formr um triângulo!\033[m'.format(primeiro_lado, segundo_lado, terceiro_lado))
else:
    print('Os segmentos {}, {} e {} \033[1;32mpodem formar um triângulo!\033[m'.format(primeiro_lado, segundo_lado, terceiro_lado))