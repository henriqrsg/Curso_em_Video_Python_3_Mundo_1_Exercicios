# AUMENTO DE FUNCIONÁRIO #

salario_atual = float(input('Digite o seu salário atual R$: '))

if salario_atual > 1250:
    novo_salario = salario_atual * 1.10
else:
    novo_salario = salario_atual * 1.15

print('O seu novo salário, após o aumento foi de \033[1;32mR${:.2f}\033[m'.format(novo_salario))