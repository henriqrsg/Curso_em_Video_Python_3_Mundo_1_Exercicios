# ESTRUTURAS CONDICIONAIS ANINHADAS #

nome = input('Qual o seu nome ? ')

if nome.upper().find('LUIZ') != -1:
    print('Seu nome é muito bonito! Parabéns!')
elif nome.upper().find('ANA') != -1 or nome.upper().find('MARIA') != -1 or nome.upper().find('JOÃO') != -1 or nome.upper().find('JOAO') != -1:
    print('Seu nome é comum demais!')
else:
    print('Seu nome é até que diferentinho!')