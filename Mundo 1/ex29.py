'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''
velocidade = int(input('Informe qual é a velocidade do carro em Km/h: '))
multa = (velocidade - 80) * 7
porcentagem = ((velocidade * 100) / 80) - 100

#calculo da multa
if velocidade > 80:
    print('\033[31m'+'Você foi multado por exceder o limite de velocidade no perimetro percorrido.\n'
          '\033[31m' + 'Limite de velocidade: '+ '\033[33m 80Km/h\n'
          '\033[31m' + 'Velocidade do veículo: \033[33m  {}Km/h, '.format(velocidade) + '{}%'.format(porcentagem) + '\033[31m' + ' à cima da velocidade.\n'
          '\033[31m' + 'Valor da multa: ' + '\033[33m R${:.2f}'.format(multa))
else:
    print('Veiculo não multado!!')