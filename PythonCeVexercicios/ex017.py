# COMPRIMENTO DA HIPOTENUSA #

cateto_oposto = int(input('Digite o valor do cateto oposto: '))
cateto_adjacente = int(input('Digite o valor do cateto adjacente: '))

hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5

print('O triângulo com catetos {} e {} tem hipotenusa {:.1f}'.format(cateto_adjacente, cateto_oposto, hipotenusa))
