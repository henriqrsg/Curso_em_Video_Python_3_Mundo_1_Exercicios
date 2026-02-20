# ALUGUEL DE CARROS #

import os

nome_programa = 'aluguel de carros'

quantidade_modelos = {}    

lista_carros = [
    {'num_marca': 1, 'num_modelo': 1, 'marca': 'toyota', 'modelo': 'corolla', 'preco_aluguel': 280},
    {'num_marca': 1, 'num_modelo': 2, 'marca': 'toyota', 'modelo': 'hilux', 'preco_aluguel': 420},
    {'num_marca': 1, 'num_modelo': 3, 'marca': 'toyota', 'modelo': 'sw4', 'preco_aluguel': 480},

    {'num_marca': 2, 'num_modelo': 1, 'marca': 'honda', 'modelo': 'civic', 'preco_aluguel': 260},
    {'num_marca': 2, 'num_modelo': 2, 'marca': 'honda', 'modelo': 'hr-v', 'preco_aluguel': 240},
    {'num_marca': 2, 'num_modelo': 3, 'marca': 'honda', 'modelo': 'city', 'preco_aluguel': 190},

    {'num_marca': 3, 'num_modelo': 1, 'marca': 'mercedes', 'modelo': 'gla', 'preco_aluguel': 520},
    {'num_marca': 3, 'num_modelo': 2, 'marca': 'mercedes', 'modelo': 'classe a', 'preco_aluguel': 450},
    {'num_marca': 3, 'num_modelo': 3, 'marca': 'mercedes', 'modelo': 'classe c', 'preco_aluguel': 600},

    {'num_marca': 4, 'num_modelo': 1, 'marca': 'bmw', 'modelo': 'serie 3', 'preco_aluguel': 580},
    {'num_marca': 4, 'num_modelo': 2, 'marca': 'bmw', 'modelo': 'x1', 'preco_aluguel': 500},
    {'num_marca': 4, 'num_modelo': 3, 'marca': 'bmw', 'modelo': 'serie 5', 'preco_aluguel': 700},

    {'num_marca': 5, 'num_modelo': 1, 'marca': 'audi', 'modelo': 'a3', 'preco_aluguel': 480},
    {'num_marca': 5, 'num_modelo': 2, 'marca': 'audi', 'modelo': 'q5', 'preco_aluguel': 620},
    {'num_marca': 5, 'num_modelo': 3, 'marca': 'audi', 'modelo': 'a4', 'preco_aluguel': 550},
]

for i in range (1,6):
    quantidade_modelos[i]= sum(1 for carro in lista_carros if carro['num_marca'] == i)

def interface():
    os.system('cls')
    print(70 * '=')
    print('{:^70}'.format(nome_programa.upper()))
    print(70 * '=')

def marcas():
    print('[1] TOYOTA')
    print('[2] HONDA')
    print('[3] MERCEDES')
    print('[4] BMW')
    print('[5] AUDI')
    print('')

def carros(num_marca):
    if num_marca not in quantidade_modelos:
        print('Desculpe, não temos este carro no estoque!')
        return False
    else:
        for carro in lista_carros:
            if carro['num_marca'] == num_marca:
                print('[{}] {}'.format(carro['num_modelo'], carro['modelo'].upper()))
        print('')
        try: 
            num_modelo = int(input('Digite o número do carro que deseja alugar [1] [2] [3]: '))
        except ValueError: 
            print('Digite apenas números! ')
            return False
        if num_modelo not in range (1, quantidade_modelos[num_marca] + 1):
            print('Desculpe, não temos este carro no estoque!')
            return False
        else:
            return num_modelo

def escolha_carro():
    interface()
    marcas()

    num_marca = int(input('Escolha o número da marca de carro que deseja: [1] [2] [3] [4] [5]: '))
    print('')

    num_modelo = carros(num_marca)

    if num_modelo == False:
        resposta = input('Deseja tentar selecionar um carro do estoque ? [S/N]: ')
        if resposta.lower() == 'sim' or resposta.lower() == 's':
            escolha_carro()
        else:
            print('Obrigado por utilizar o software !!')
    else: 
        print('')
        for carro in lista_carros:
            if carro['num_marca'] == num_marca and carro['num_modelo'] == num_modelo:
                print('Parabéns voce escolheu o carro {} da marca {}'.format(carro['modelo'].upper(), carro['marca'].upper()))
        input('')
        interface()
        valor_aluguel(num_modelo, num_marca)

def valor_aluguel(num_modelo, num_marca):
    for carro in lista_carros:
        if carro['num_marca'] == num_marca and carro['num_modelo'] == num_modelo:
            dias_alugados = int(input('O valor do aluguel do carro {} é de R${:.2f} por dia, sendo assim,\n' \
            'por quantos dias você deseja alugar o carro ? '.format(carro['modelo'].upper(), carro['preco_aluguel'])))
            valor_aluguel = dias_alugados * carro['preco_aluguel']

            print('O preço final do aluguel do carro {}, alugando por {} dias é de R${:.2f}!'.format(carro['modelo'].upper(), dias_alugados, valor_aluguel))



escolha_carro()