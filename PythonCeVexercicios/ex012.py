# Novo preço produto #

import os

nome_programa = 'desconto em loja'

lista_produtos = [
    {'num': 1, 'nome': 'pao', 'preco': 0.5},
    {'num': 2, 'nome': 'leite', 'preco': 5},
    {'num': 3, 'nome': 'cafe', 'preco': 25},
    {'num': 4, 'nome': 'presunto', 'preco': 1},
    {'num': 5, 'nome': 'margarina', 'preco': 10}
]

desconto = 0.12
quant_produtos = len(lista_produtos)

def interface():
    os.system('cls')
    print(50 * '=')
    print('{:^50}'.format(nome_programa.upper()))
    print(50 * '=')
    print('')

    for produto in lista_produtos:
        print('[{}] {}'.format(produto['num'], produto['nome'].upper()))

    return int(input('Qual produto você deseja comprar ? [Digite um número]: '))

def quer_comprar_mais(valor_total):
    resposta = input('Deseja comprar outro produto ? [S/N]: ')
    if resposta.lower() == 's':
        num_produto = interface()
        produto(num_produto, valor_total)
    elif resposta.lower() == 'n':
        os.system('cls')
        print('O total de sua compra foi de R${:.2f} !'.format(valor_total))
        if valor_total == 0:
            print('Obrigador por vir em nosso estabelecimento! Volte sempre!')
        else: 
            valor_total = valor_total * (1 - desconto)
            print('Porém hoje estamos tendo desconto no valor de {:.2f}%'.format(desconto * 100))
            print('Logo sua compra irá ficar no valor de R${:.2f}'.format(valor_total))
            print('Obrigador por comprar em nosso estabelecimento! Volte sempre!')

def produto(num_produto, valor_total):
    if num_produto <= quant_produtos:
        for produto in lista_produtos:
            if produto['num'] == num_produto:
                print('O valor do {} está de R${:.2f} a unidade! '.format(produto['nome'].upper(), produto['preco']))
                quantidade_item = int(input('Quantas unidades de {} você deseja ? '.format(produto['nome'].upper())))
                valor_produto = quantidade_item * produto['preco']
                print('O preço de {} unidades de {} é igual a R${:.2f}'.format(int(quantidade_item), produto['nome'], valor_produto))
                valor_total += valor_produto
                quer_comprar_mais(valor_total)
    else:
        print('Não temos esse produto no estoque! =(')
        quer_comprar_mais(valor_total)

num_produto = interface()
produto(num_produto, valor_total = 0)