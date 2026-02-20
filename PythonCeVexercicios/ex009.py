# Tabuada #

nome_do_programa = 'TABUADA'
numero = int(input('Digite o número que deseja ver a tabuada: '))
print('')
print(25 * '=')
print('A {} DO NÚMERO {}'.format(nome_do_programa, numero).center(25))
print(25 * '=')
print('')
for i in range(1, 11):
    print('{} x {:2} = {:2}' .format(numero, i, numero * i).center(25))
print('')
print(25 * '=')