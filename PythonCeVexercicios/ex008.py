# Conversor de unidades de comprimento #

nome_p = 'CONVERSOR DE MEDIDAS'
print(30 * '=')
print('{:^30}'.format(nome_p))
print(30 * '=')
metros = float(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print('O valor de {:.2f}m correspondem a {:.2f}cm e {:.2f}mm'.format(metros, centimetros, milimetros)) 