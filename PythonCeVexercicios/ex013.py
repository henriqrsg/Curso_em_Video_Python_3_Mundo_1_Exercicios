# Aumento de salário #

import os
from datetime import datetime

ano_atual = datetime.now().year

nome_programa = 'reajuste salarial'
nome_second_interface = 'parte do funcionário'

reajuste = 0.02

def interface():
    os.system('cls')
    print(70 * '=')
    print('{:^70}'.format(nome_programa.upper()))
    print(70 * '=')
    quant_func = int(input('Digite a quantidade de funcionários que você tem na sua empresa: '))
    return quant_func

def second_interface():
    os.system('cls')
    print(100 * '=')
    print('{:^100}'.format(nome_second_interface.upper()))
    print(100 * '=')
    ano = int(input('Digite em qual ano você deseja ver o valor do seu salário de acordo com o reajuste de {}% ao ano: '. format(reajuste)))
    return ano

quant_func = interface()

salario = []

for i in range(quant_func):
    salario.append(float(input('Digite o salário do {}º funcionário: '.format(i+1))))

ano = second_interface()
while ano < ano_atual:
    input('Esse ano já passou, trabalhe com anos futuros!')
    ano = second_interface()
numero_func = int(input('Digite qual o seu número de funcionário: '))

salario_reajustado = salario[numero_func - 1] * ((1 + reajuste) ** (ano - ano_atual))

print('O seu salário de R${:.2f} no ano de {} com o reajuste de {:.2f}% ano ano será de R${:.2f}!'.format(salario[numero_func - 1], ano, reajuste, salario_reajustado))