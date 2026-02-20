# DISSECAÇÃO DE NOME #

nome_programa = 'características do nome'.upper()

def interface():
    print(50 * '=')
    print('{:^50}'.format(nome_programa))
    print(50 * '=')

interface()

nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome somente com letras minusculas é {}'.format(nome.lower()))
print('Seu nome somente com letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], nome.find(' ')))