n1 = int(input("Informe o primeiro numero "))
n2 = int(input("Informe o segundo numero "))
potencia = n1 ** n2
divInteiro = n1 // n2
divResto = n1 % n2
raizQuadrada = n1**(1/2)

print('Potencia {} \n'
      'Resultado da divisao inteira {} \n'
      'Resto da divisao {} \n'
      'Raiz quadrada do primeiro numero é {:.0f}!'.format(potencia,divInteiro,divResto, raizQuadrada))