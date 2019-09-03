#fazer um programa que mostre o dobro, o triplo e a raiz quadrada do valor digitado.
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero **(1/2)
raizCubica = numero **(1/3)

print('O número digitado foi {} \n O dobro deste número é {:=^10}\n O triplo deste número é {:=^10}\n A Raiz quadrada deste número é {:.2f}\n A Raiz cubica deste número é {:.2f} '.format(numero,dobro,triplo,raizQuadrada,raizCubica))
