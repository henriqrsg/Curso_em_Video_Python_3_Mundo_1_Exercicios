# LEITOR DE 3 NÚMEROS #

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))

if numero_1 > numero_2 and numero_1 > numero_3:
    ultimo = numero_1
elif numero_2 > numero_1 and numero_2 > numero_3:
    ultimo = numero_2
else:
    ultimo = numero_3

if numero_1 < numero_2 and numero_1 < numero_3:
    primeiro = numero_1
elif numero_2 < numero_1 and numero_2 < numero_3:
    primeiro = numero_2
else:
    primeiro = numero_3

if (numero_1 > numero_2 and numero_1 < numero_3) or (numero_1 > numero_3 and numero_1 < numero_2):
    meio = numero_1 
elif (numero_2 > numero_1 and numero_2 < numero_3) or (numero_2 > numero_3 and numero_2 < numero_1):
    meio = numero_2
else:
    meio = numero_3

print('Os números digitados em ordem crescente são: {}, {} e {}'.format(primeiro, meio, ultimo))