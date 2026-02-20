# Calculo de média de notas #

nome_programa = 'CÁLCULO DE MÉDIA'
print('=' * 55)
print('{:^55}'.format(nome_programa))
print('=' * 55)
print(' ')
quant_n = int(input('Digite quantos números voce irá querer calcular a média: '))

soma = 0
for n in range(quant_n):
    numero = int(input('Digite o {}º número: '.format(n+1)))
    soma = soma + numero
    media = soma / quant_n

print('A média dos números é igual a {}'.format(media))