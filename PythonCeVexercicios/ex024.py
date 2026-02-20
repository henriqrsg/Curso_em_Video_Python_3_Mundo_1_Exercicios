# CIDADE COMEÇA OU NÃO COM A PALAVRA SANTO #

cidade = input('Digite o nome da sua cidade: ').strip()
if cidade[:5].upper() == 'SANTO':
    print('Sua cidade começa com a palavra Santo')
else:
    print('Sua cidade não começa com a palavra Santo')

