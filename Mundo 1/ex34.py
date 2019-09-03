'''Escrea um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salário superior à 1.250, calcule o almento de 10%.
Para salário igua ou inferior à 1.250, calcule o aumento de 15%'''

salario = float(input('Informe o salário do funcionário: '))

if salario > 1250:
    reajuste = 10
    novo_valor = ((salario * reajuste) / 100) + salario
else:
    reajuste = 15
    novo_valor = ((salario * reajuste) / 100) + salario

print('O novo salário passou para \033[032m R${:.2f}\033[m com o reajuste de {:.2f}%'.format(novo_valor,reajuste))

