nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('')
print('{} vamos fazer operações aritméticas!'.format(nome))

titulo = 'Operações Aritméticas'
print('=' * 25)
print('{:^25}'.format(titulo)) 
print('=' * 25)
print('')
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
exponenciacao = numero1 ** numero2
print('')
print('A soma entre {} e {} é igual a {}'.format(numero1, numero2, soma))
print('A subtração entre {} e {} é igual a {}'.format(numero1, numero2, subtracao))
print('A multiplicação entre {} e {} é igual a {}'.format(numero1, numero2, multiplicacao))
print('A divisão entre {} e {} é igual a {:.2f}'.format(numero1, numero2, divisao))
print('A divisão inteira entre {} e {} é igual a {}'.format(numero1, numero2, divisao_inteira))
print('A exponenciação de {} elevado a {} é igual a {}'.format(numero1, numero2, exponenciacao))