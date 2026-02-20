# Leitor de primeiro e último nome #

nome = input('Digite o seu nome: ')

print('O seu primeiro nome é {} e o seu último nome é {}'.format(nome.split()[0], nome.split()[-1]))