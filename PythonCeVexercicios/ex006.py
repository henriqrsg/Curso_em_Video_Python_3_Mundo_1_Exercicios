# Algoritmo que mostra seu dobro, triplo e raiz quadrada #

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz_q = numero ** (1/2)

print('O número {} tem como dobro {} e como triplo {}, além disso possui raiz quadrada de {:.2f}'.format(numero, dobro, triplo, raiz_q))