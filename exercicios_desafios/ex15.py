'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.'''


print('-'*20 + ' Este é o BH locadora de veiculos '+ '-'*20)
diasRodados = float(input('Favor informar por quantos os dias o carro foi alugado: '))
kmRodados = float(input('Favor informar quantos Kms foi percorrido: '))
custoDia = diasRodados * 60
custoKm = kmRodados * 0.15
custoTotal = custoDia + custoKm
print('\nO valor total pelos dias usados foi:         R$ {:.2f}\n'
      'O valor total pela Quilometragem rodada foi: R$ {:.2f}\n'
      'O valor total do aluguém do carro é:         R$ {:.2f} '.format(custoDia,custoKm,custoTotal))

