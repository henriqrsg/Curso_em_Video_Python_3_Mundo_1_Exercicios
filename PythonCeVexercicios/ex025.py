# SEU NOME TEM SILVA #

nome = input('Digite o seu nome: ') 

if nome.upper().find('SILVA') == -1:
    print('Seu nome não tem \033[1;31mSilva\033[m')
else:
    print('Seu nome tem \033[1;32mSilva\033[m')