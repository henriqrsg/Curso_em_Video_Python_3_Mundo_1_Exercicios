# Quantidade de tinta #

nome_programa = 'CÁLCULO PARA PINTURA'
print(30 * '=')
print('{:^30}'.format(nome_programa))
print(30 * '=')
print('')
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
medida = input('Você me deu os valores em m ou cm ? ')
if medida.lower() == 'cm':
    altura = altura / 100
    largura = largura / 100
area = altura * largura
preco = 2
valor_total = area * preco
print('A sua parede tem área total de {:.2f}m² e portanto como cada m² custa {:.2f}, a pintura irá sair no valor de R${:.2f}'.format(area, preco, valor_total))
