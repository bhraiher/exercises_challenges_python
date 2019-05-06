#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n1 = int(input('Informe a metragem: '))
cm = n1*100
mm = n1*1000
print('Numero digitado: {}\n'
      'Em centímetros: {:.0f}\n'
      'Em milímetro: {:.0f}'.format(n1,cm,mm))