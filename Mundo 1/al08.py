import math
import random
# noinspection PyUnresolvedReferences

num = int(input('Informe um número: '))
raiz = math.sqrt(num) #utilizou a bilbioteca para verificar a raiz quadrada do número diditado.
print('A raiz quadrada de {} é igual à {}'.format(num, math.ceil(raiz))) #usou a biblioteca para arredondar para cima.

num2 = random.randint(1,100)
print(num2)

