# Somando números #

print(33 * '=')
print(6 * ' ', 'VAMOS SOMAR NÚMEROS', 6 * ' ')
print(33 * '=')

soma = 0
numero = int(input('Digite um número: '))
soma = soma + numero

continuar = input('Deseja continuar ? [S/N]: ')
while continuar.lower() == 's' or continuar.lower() == 'sim':
    if continuar.lower() == 's' or continuar.lower() == 'sim':
        numero = int(input('Digite um número: '))
        soma = soma + numero
        continuar = input('Deseja continuar ? [S/N]: ')

print('A soma dos números é igual a {}'.format(soma))