# Conversor de moedas # 

nome = 'CONVERSOR DE MOEDAS'
print(25 * '=')
print('{:^25}'.format(nome))
print(25 * '=')
print('')
Qual_moeda = input('Qual moeda você está em mãos ? [Dólar, Real, Euro]: ')

if Qual_moeda.lower() == 'dólar' or Qual_moeda.lower() == 'd' or Qual_moeda.lower() == 'dolar':
    dolar = float(input('Quanto você tem em Dólares ? U$'))
    real = dolar * 5.16
    euro = dolar * 0.84
    print('U${:.2f} equivalem a R${:.2f} e a E${:.2f} !'.format(dolar, real, euro))
elif Qual_moeda.lower() == 'real' or Qual_moeda.lower() == 'r':
    real = float(input('Quanto você tem em Reais ? R$'))
    dolar = real / 5.16
    euro = real / 6.13
    print('R${:.2f} equivalem a U${:.2f} e a E${:.2f} !'.format(real, dolar, euro))
elif Qual_moeda.lower() == 'euro' or Qual_moeda.lower() == 'e':
    euro = float(input('Quanto você tem em Euros ? E$'))
    real = euro * 6.13
    dolar = euro / 0.84
    print('E${:.2f} equivalem a R${:.2f} e a U${:.2f} !'.format(euro, real, dolar))
else:
    print('Infelizmente não temos conversor para esta moeda! 😔')
