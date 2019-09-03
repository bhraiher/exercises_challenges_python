'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km
e R$0,40 para viagens mais longas.'''
dist = int(input('Qual é a distância da viagem: '))

if  dist > 0  and dist <= 200:
    print('O valor da viagem ficou R${:.2f}'.format(dist * 0.50)) #calcula o valor da passagem multiplicado pela distância
elif dist > 200:
    print('O valor da viagem ficou R${:.2f}'.format(dist * 0.45)) #calcula o valor da passagem multiplicado pela distância
