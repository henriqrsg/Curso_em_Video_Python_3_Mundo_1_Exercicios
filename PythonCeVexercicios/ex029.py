# CALCULO DE MULTA #

velocidade = float(input('Digite a velocidade do seu carro em km/h: '))

if velocidade > 80:
    velocidade_excedidada = velocidade - 80
    multa = velocidade_excedidada * 7
    print('Você foi multado em R${:.2f} por estár {:.1f} km/h acima do limite de velodicade'.format(multa, velocidade_excedidada))
else:
    print('Parabéns! Você é um bom motorista e não foi multado!')