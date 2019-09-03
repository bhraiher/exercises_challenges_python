'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte
o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o emprestimo será negado.'''

'''Bonûs do exercício: Verificar a faixa de juros.'''
import time

#Requisitar: Valor da casa, salário do comprador e em quantos anos ele irá pagar.
#Condição: O valor da parcela não pode ultrapassar os 30% do salário.

#Colhendo os dados
vlrCasa = float(input('Valor do imóvel: R$ '))
vlrSalCli = float(input('Salário cliente: R$ '))
qtdAnos = int(input('Anos para quitação: '))

if qtdAnos <= 10:
    juros = 1.30
elif qtdAnos > 10 and qtdAnos <= 15:
    juros = 1.50
elif qtdAnos > 15:
    juros = 1.95

print('\nO juros mensal para esse financiamento é de {}% mensal.'.format(juros))

print('Processando financiamento...')
time.sleep(3)
#realizando a condição
parcela = (vlrCasa / (qtdAnos * 12)) * juros / 100 + (vlrCasa / (qtdAnos * 12)) if juros > 0 else (vlrCasa / (qtdAnos * 12))
parcSal = (vlrSalCli * 30) / 100

print('Valor parcela: R$ {:.2f} \n'.format(parcela) +
      'O salário permite uma parcela de no máximo R$ {:.2f}'.format(parcSal))
if parcela > parcSal:
    print('Financiamento \033[31m NEGADO! \033[m Sugerido dividir em uma quantidade maior de anos.')
else:
    print('Financiamento \033[32m APROVADO!')



