# ANO BISSEXTO #

ano_atual = int(input('Digite o ano em que estamos atualmente: '))

if (ano_atual % 4 == 0) and (ano_atual % 100 != 0) or (ano_atual % 400 == 0):
    print('O ano {} é bissexto.'.format(ano_atual))
else:
    print('O ano {} não é bissexto.'.format(ano_atual))