# CONVERSOR DE TEMPERATURA #

import os

nome_programa = 'conversor de temperatura'

def interface ():
    os.system('cls')
    print(70 * '=')
    print('{:^70}'.format(nome_programa.upper()))
    print(70 * '=')
    print('')
    print('[1] -> GRAUS CELSIUS')
    print('[2] -> GRAUS FAHRENHEIT')
    print('[3] -> KELVIN')
    print('')

def escolha_medida():
    resposta = int(input('Digite o número da medida de temperatura você deseja converter ? [1] [2] [3]: '))
    return resposta

def conversor(resposta):
    if resposta == 1:
        valor_celsius = float(input('Digite quantos Graus Celsius você deseja converter: '))
        valor_fahrenheit = valor_celsius * 1.8 + 32
        valor_kelvin = valor_celsius + 273.15
        print('A temperatuda de {:.2f}ºC é igual a {:.2f}ºF e {:.2f}K !'.format(valor_celsius, valor_fahrenheit, valor_kelvin))
    elif resposta == 2:
        valor_fahrenheit = float(input('Digite quantos Graus Farenheit você deseja converter: '))
        valor_celsius = (valor_fahrenheit - 32) / 1.8
        valor_kelvin = (valor_fahrenheit + 459.67) / 1.8
        print('A temperatuda de {:.2f}ºF é igual a {:.2f}ºC e {:.2f}K !'.format(valor_fahrenheit, valor_celsius, valor_kelvin))
    elif resposta == 3: 
        valor_kelvin = float(input('Digite quantos Kelvin você deseja converter: '))
        valor_celsius = valor_kelvin - 273.15
        valor_fahrenheit = valor_kelvin * 1.8 - 459.67
        print('A temperatuda de {:.2f}K é igual a {:.2f}ºC e {:.2f}F !'.format(valor_kelvin, valor_celsius, valor_fahrenheit))
    else:
        print('Desculpe mas não trabalhamos com esta temperatura! ')

interface()

conversor(escolha_medida())
