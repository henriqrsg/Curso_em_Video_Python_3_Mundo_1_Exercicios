# LEITOR DE NÚMERO #

numero = int(input('digite um número de 0 a 9999: '))

unidade = numero // 1 % 10

dezena = numero // 10 % 10

centena = numero // 100 % 10

milhar = numero // 1000 % 10

print('Analisando o número {} podemos afirmar o seguinte'.format(numero))
print('Sua unidade é {}'.format(unidade))
print('Sua dezena é {}'.format(dezena))
print('Sua centena é {}'.format(centena))
print('Sua milhar é {}'.format(milhar))


