# CALCULADORA DE PREÇO DE VIAGENS #

distancia = float(input('Digite a distância da sua viagem em km: '))

if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia

print('A distância de \033[1;36m{:.1f}\033[m km que você deseja percorrer terá o custo de \033[1;31mR${:.2f}\033[m'.format(distancia, preco))